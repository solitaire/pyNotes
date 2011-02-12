# -*- coding: utf-8 -*-  
#       Copyright 2010 Anna Stępień <solitaire at g.pl>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import datetime
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from elixir import *
from sqlalchemy import desc
from note import *
from notebook import *
from tag import *

dbdir=os.path.join(os.path.expanduser("~"),".pynotes")
dbfile=os.path.join(dbdir,"notes.sqlite")

if not os.path.isdir(dbdir):
    os.mkdir(dbdir)
metadata.bind = "sqlite:///%s"%dbfile
metadata.bind.echo = True
setup_all(True)
if not os.path.exists(dbfile):
    create_all()
    

NOTE_COLUMNS = ["Title", "Notebook", "Created at", "Updated at"]

class NoteModel(QAbstractTableModel, QSortFilterProxyModel):
    def __init__(self):
        super(QAbstractTableModel, self).__init__()
        self.notes = []
        self.load()

    def rowCount(self, index=QModelIndex()):
        return len(self.notes)

    def columnCount(self, index=QModelIndex()):
        return 6

    def data(self, index, role=Qt.DisplayRole):
        note = self.getNote(index)
        if not note:
            return QVariant()
        column = index.column()

        if role == Qt.DisplayRole or role == Qt.EditRole:
            if column == TITLE:
                return QVariant(note.title)
            elif column == NOTEBOOK:
                if note.notebook is not None:
                    return QVariant(note.notebook.name)
                else:
                    return QVariant()
            elif column == BODY:
                return QVariant(note.body)
            elif column == CREATED_AT:
                return QVariant(QDate(note.created_at).toString(u'yyyy-MM-dd'))
            elif column == UPDATED_AT:
                return QVariant(QDate(note.updated_at).toString(u'yyyy-MM-dd'))
            elif column == TAGS:
                return QVariant(','.join( [tag.name for tag in note.tags]))

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(NOTE_COLUMNS[section])

    def insertRows(self, position, new_note, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows -1)
        for row in range(rows):
            self.notes.insert(position + row, new_note)
        self.endInsertRows()
        self.load()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.notes[position].delete()
        self.notes = self.notes[:position] + self.notes[position + rows:]
        self.endRemoveRows()
        session.commit()
        return True


    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractListModel.flags(self, index) | Qt.ItemIsEditable)

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.notes):
            note = self.getNote(index)
            column = index.column()
            if column == TITLE:
                note.title = "%s" % (value.toString())
            elif column == BODY:
                note.body = "%s" % (value.toString())
            elif column == NOTEBOOK:
                notebook = Notebook.get_by(name = "%s" % (value.toString()))
                note.notebook = notebook
            elif column == TAGS:
                #split into tags
                tags = []
                for tag_name in value.toString().split(",", QString.SkipEmptyParts):
                    tag_name = ("%s"% tag_name).strip()
                    tag = self.tag_model.getByName(tag_name)
                    if not tag:
                        tag = Tag(name=tag_name)
                        #access directly to the tag model
                        #in order to emit dataChanged signal properly
                        row = self.tag_model.rowCount()
                        self.tag_model.insertRows(row, tag)
                        self.emit(SIGNAL("dataChanged(QModelIndex, QModelIndex"), self.tag_model.index(row), self.tag_model.index(row))
                    tags.append(tag)
                note.tags = tags
            try:
                session.commit()
            except:
                session.rollback()
            self.emit(SIGNAL("dataChanged(QModelIndex, QModelIndex"), index, index)
            return True
        return False


    def getNote(self, index):
        if not index.isValid() or not ( 0 <= index.row() <= len(self.notes)):
            return None
        return self.notes[index.row()]
    
    def getById(self, id):
        return self.notes[id]


    def getByNotebook(self, index):
        self.beginResetModel()
        notebook_name= "%s" % (index.data().toString())
        nb = Notebook.get_by(name=notebook_name)
        self.notes = Note.query.filter_by(notebook=nb).all() 
        session.commit()
        self.endResetModel()
              

    def getByTag(self,index):
        self.beginResetModel()
        tag_name = "%s" % (index.data().toString())
        self.notes = Note.query.filter(Note.tags.any(name=tag_name)).all()
        session.commit()
        self.endResetModel()

    def uncategorized(self):
        self.beginResetModel()
        self.notes = Note.query.filter(Note.notebook == None).all()
        session.commit()
        self.endResetModel()

    def search(self, query):
        self.reset()
        self.notes = Note.query.filter(Note.body.like("%{0}%".format(query))).all()
        session.commit()

    def clear(self):
        self.notes = []

    def load(self):
        self.beginResetModel()
        self.notes = Note.query.order_by(desc(Note.created_at)).all()
        session.commit()
        self.endResetModel()

    def save(self):
        session.commit()
    
    #dirty helper method used for direct access to tag model
    def addTagging(self, tag_model):
        self.tag_model = tag_model
        


class NotebookModel(QAbstractListModel):
    def __init__(self):
        super(QAbstractListModel, self).__init__()
        self.notebooks = []
        self.load()

    def rowCount(self, index=QModelIndex()):
        return len(self.notebooks)

    def data(self, index, role=Qt.DisplayRole):
        notebook = self.getNotebook(index)

        if not notebook:
            return QVariant()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return QVariant(notebook.name)
        elif role == Qt.DecorationRole:
            return QIcon(":/icons/folder.png")

        return QVariant()

    def insertRows(self, position, new_notebook, rows=1, index=QModelIndex()):
        self.beginInsertRows(index, position, position + rows - 1)
        for row in range(rows):
            self.notebooks.insert(position + rows - 1, new_notebook)
        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.notebooks[position].delete()
        self.notebooks = self.notebooks[:position] + self.notebooks[position + rows:]
        self.endRemoveRows()

        return True

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractListModel.flags(self, index) | Qt.ItemIsEditable)

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.notebooks):
            notebook = self.getNotebook(index)
            column = index.column()
            if column == NAME:
                notebook.name = "%s" % (value.toString())
            try:
                session.commit()
            except:
                session.rollback()
            self.emit(SIGNAL("dataChanged(QModelIndex, QModelIndex"), index, index)
            return True
        return False

    def getNotebook(self, index):
        if not index.isValid() or not ( 0 <= index.row() <= len(self.notebooks)):
            return None
        return self.notebooks[index.row()]


    def load(self):
        self.notebooks = Notebook.query.all()


class TagModel(QAbstractListModel):
    def __init__(self):
        super(QAbstractListModel,self).__init__()
        self.tags =[]
        self.load()

    def rowCount(self, index = QModelIndex()):
        return len(self.tags)

    def data(self, index, role=Qt.DisplayRole):
        tag = self.getTag(index)

        if not tag:
            return QVariant()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return QVariant(tag.name)
        elif role == Qt.DecorationRole:
            return QIcon(":/icons/tag_blue.png")
        return QVariant()

    def insertRows(self, position, new_tag, rows=1, index=QModelIndex()):
        self.beginInsertRows(index, position, position + rows - 1)
        for row in range(rows):
            self.tags.insert(position + rows - 1, new_tag)
        self.endInsertRows()
        session.commit()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        tag_name = "%s" % (index.data().toString())
        notes = Note.query.filter(Note.tags.any(name=tag_name)).all()
        for note in notes:
            note.tags.remove(self.tags[position])
        self.tags[position].delete()
        self.tags = self.tags[:position] + self.tags[position + rows:]
        self.endRemoveRows()
        session.commit()
        return True

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractListModel.flags(self, index) | Qt.ItemIsEditable)

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.tags):
            tag = self.getTag(index)
            column = index.column()
            if column == NAME:
                tag.name = "%s" % (value.toString())
            try:
                session.commit()
            except:
                session.rollback()
            self.emit(SIGNAL("dataChanged(QModelIndex, QModelIndex"), index, index)
            return True
        return False

    def getTag(self, index):
        if not index.isValid() or not ( 0 <= index.row() <= len(self.tags)):
            return None
        return self.tags[index.row()]
    
    def getByName(self, tag_name):
        return Tag.query.filter_by(name=tag_name).first()


    def load(self):
        self.reset()
        self.tags =Tag.query.all()
        
        
class NoteProxyModel():
    pass

