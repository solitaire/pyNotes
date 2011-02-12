# -*- coding: utf-8 -*-
#       
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

from PyQt4 import QtCore, QtGui
from model.model import *
from model.note import *

class NoteMapper:    
    def __init__(self, parent, model, widgets):
        self.mapper = QtGui.QDataWidgetMapper(parent)
        self.mapper.setSubmitPolicy(QtGui.QDataWidgetMapper.AutoSubmit)
        self.mapper.setModel(model)
        self.mapper.setItemDelegate(NotebookDelegate(parent))
        self.mapper.addMapping(widgets[0], BODY)
        self.mapper.addMapping(widgets[1], TITLE)
        self.mapper.addMapping(widgets[2], NOTEBOOK)
        self.mapper.addMapping(widgets[3], TAGS)
        
    def setCurrentIndex(self, index):
        self.mapper.setCurrentIndex(index)
        
    def currentIndex(self):
        return self.mapper.currentIndex()
    
    def toFirst(self):
        self.mapper.toFirst()
    
    def toLast(self):
        self.mapper.toLast()
 
# Custom delegate class
# Overwrites default behaviour of presenting note's notebook
              
class NotebookDelegate(QtGui.QItemDelegate):
    def __init__(self,parent=None):
        super(NotebookDelegate, self).__init__(parent)
        self.parent = parent
        
    def setEditorData(self, editor, index):
        if index.column() == NOTEBOOK:
            value = index.model().data(index,Qt.DisplayRole).toString() 
            item_index = editor.findText(value)
            editor.setCurrentIndex(item_index)
        elif index.column() == TAGS:
            editor.setText(index.model().data(index, Qt.DisplayRole).toString())
        else:
            QtGui.QItemDelegate.setEditorData(self, editor, index)
    
    def setModelData(self, editor, model, index):
        if index.column() == NOTEBOOK:
            model.setData(index, QVariant(editor.currentText()))
        elif index.column() == TAGS:
            model.setData(index, QVariant(editor.text()))
        else:
            QtGui.QItemDelegate.setModelData(self, editor, model, index)
            