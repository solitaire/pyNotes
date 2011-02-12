#!/usr/bin/env python
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


import sys
from PyQt4 import QtCore, QtGui
from view.notes_ui import Ui_Notebook
from model import *
from notebook_dialog import *
from tag_dialog import *
from note_view import *
from note_mapper import *
from rich_formatting import *
from exporter import *
from snippet import *
from tray import *

		
class NotesMain(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		#create actions
		self.createActions()
		self.initMVC()	
		#slots
		self.connectSlots()
		#tray
		self.tray = ApplicationTray(self)
		
		
	def connectSlots(self):
		self.ui.notebooks.clicked.connect(self.filterByNotebook)
		self.ui.tags.clicked.connect(self.filterByTag)
		self.ui.notes.clicked.connect(self.editInPlace)
		self.ui.notes.doubleClicked.connect(self.editInNewWindow)
		self.ui.all_notes.clicked.connect(self.show_all_notes)
		self.ui.uncategorized_notes.clicked.connect(self.show_uncategorized_notes)
		self.ui.action_new_notebook.triggered.connect(self.createNotebook)
		self.ui.action_new_note.triggered.connect(self.createNote)
		self.ui.action_close.triggered.connect(self.quit)
		self.destroyNotebookAction.triggered.connect(self.destroyNotebook)
		self.destroyNoteAction.triggered.connect(self.destroyNote)
		self.destroyTagAction.triggered.connect(self.destroyTag)
		self.addNoteToNotebookAction.triggered.connect(self.addNoteToNotebook)
		self.ui.removeNoteFromNotebookButton.clicked.connect(self.removeNoteFromNotebook)
		self.ui.searchButton.clicked.connect(self.search)
		self.ui.snippetButton.clicked.connect(self.addSnippet)
		self.ui.actionNew_tag.triggered.connect(self.createTag)
		
	
	def createActions(self):
		self.destroyNotebookAction = QtGui.QAction("Delete notebook", self)
		self.addNoteToNotebookAction = QtGui.QAction("Add note", self)
		self.destroyNoteAction =  QtGui.QAction("Delete note", self)
		self.destroyTagAction = QtGui.QAction("Delete tag", self)
		
	def initMVC(self):
		self.ui = Ui_Notebook()
		self.ui.setupUi(self)
		
		#assign models to views
		self.notes_model = NoteModel()
		self.notebooks_model = NotebookModel()
		self.tags_model = TagModel()
		self.notes_model.addTagging(self.tags_model)

		
		self.ui.notes.setModel(self.notes_model)
		self.ui.notebooks.setModel(self.notebooks_model)
		self.ui.tags.setModel(self.tags_model)
		self.ui.notes.setColumnHidden(BODY, True)
		self.ui.notes.setColumnHidden(TAGS, True)
		
		self.note_mapper = NoteMapper(self, self.notes_model, [self.ui.notesTextEdit, self.ui.titleEdit, self.ui.notebooksBox, self.ui.notesTags])
		self.note_mapper.toFirst()
		#initial state must be set manually
		self.ui.notebooksBox.setModel(self.notebooks_model)
		index = self.notes_model.index(self.note_mapper.currentIndex(),0)
		self.note_mapper.setCurrentIndex(index.row())
		
		self.rich_edit = RichFormatting(self.ui)
		self.note_exporter = NoteExporter(self, self.ui)
		
		#context menus
		self.createContextMenuForNotebooks()
		self.createContextMenuForNotes()
		self.createContextMenuForTags()

	
	@QtCore.pyqtSlot()
	def createContextMenuForNotebooks(self):
		self.ui.notebooks.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ui.notebooks.customContextMenuRequested.connect(self.onContextNotebook)
		self.menu = QtGui.QMenu("Menu", self.ui.notebooks)
		self.menu.addAction(self.destroyNotebookAction)
		self.menu.addAction(self.addNoteToNotebookAction)
		
	@QtCore.pyqtSlot()
	def createContextMenuForNotes(self):
		self.ui.notes.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ui.notes.customContextMenuRequested.connect(self.onContextNote)
		self.menu_for_note = QtGui.QMenu("Menu note", self.ui.notes)
		self.menu_for_note.addAction(self.destroyNoteAction)
		
	@QtCore.pyqtSlot()
	def createContextMenuForTags(self):
		self.ui.tags.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ui.tags.customContextMenuRequested.connect(self.onContextTag)
		self.menu_for_tag = QtGui.QMenu("Menu", self.ui.tags)
		self.menu_for_tag.addAction(self.destroyTagAction)
	
	@QtCore.pyqtSlot("const QPoint&")
	def onContextNotebook(self):
		self.menu.exec_(QtGui.QCursor.pos())

	@QtCore.pyqtSlot("const QPoint&")
	def onContextTag(self):
		self.menu_for_tag.exec_(QtGui.QCursor.pos())
		
	@QtCore.pyqtSlot("const QPoint&")
	def onContextNote(self):
		self.menu_for_note.exec_(QtGui.QCursor.pos())
	
	@QtCore.pyqtSlot("const QModelIndex &")
	def filterByNotebook(self, index):
		self.notes_model.getByNotebook(index)
	
	@QtCore.pyqtSlot("const QModelIndex &")	
	def filterByTag(self, index):
		self.notes_model.getByTag(index)
	
	@QtCore.pyqtSlot("const QModelIndex &")
	def editInPlace(self, index):
		self.note_mapper.setCurrentIndex(index.row())
	
	@QtCore.pyqtSlot("const QModelIndex &")	
	def editInNewWindow(self, index):
		note_form = NoteForm(self, self.notes_model,self.notebooks_model, index)
		note_form.show()
	
	@QtCore.pyqtSlot()
	def show_all_notes(self):
		self.notes_model.load()
		
	@QtCore.pyqtSlot()
	def show_uncategorized_notes(self):
		self.notes_model.uncategorized()
		
	@QtCore.pyqtSlot()
	def createNotebook(self):
		notebook_form = NotebookDialog(self, notebook_model=self.notebooks_model)
		notebook_form.show()
	
	@QtCore.pyqtSlot()
	def createTag(self):
		tag_form = TagDialog(self, self.tags_model)
		tag_form.show()
	
	@QtCore.pyqtSlot()	
	def createNote(self):
		note = Note()
		session.commit()
		row = self.notes_model.rowCount()
		self.notes_model.insertRows(row, note)
	
	@QtCore.pyqtSlot()
	def addSnippet(self):
		snippet_form = SnippetDialog(self, self.ui.notesTextEdit)
		snippet_form.show()
	
	@QtCore.pyqtSlot()
	def destroyNotebook(self):
		self.notebooks_model.removeRows(self.ui.notebooks.currentIndex().row(), 1)
	
	@QtCore.pyqtSlot()	
	def destroyNote(self):
		self.notes_model.removeRows(self.ui.notes.currentIndex().row(), 1)
	
	@QtCore.pyqtSlot()	
	def destroyTag(self):
		self.tags_model.removeRows(self.ui.tags.currentIndex().row(), 1)
	
	@QtCore.pyqtSlot()
	def addNoteToNotebook(self):
		note = Note()
		#append choosen notebook to a new created note
		choosen_notebook = self.notebooks_model.getNotebook(self.ui.notebooks.currentIndex())
		note.notebook = choosen_notebook
		session.commit()
		self.notes_model.insertRows(self.notes_model.rowCount(), note)
	
	@QtCore.pyqtSlot()
	def removeNoteFromNotebook(self):
		index = self.ui.notes.currentIndex()
		note = self.notes_model.getNote(index)
		note.notebook = None
		self.note_mapper.setCurrentIndex(index.row())
		session.commit()
		
	@QtCore.pyqtSlot()	
	def search(self):
		query = self.ui.searchField.text()
		self.notes_model.search(query)
	
	@QtCore.pyqtSlot()
	def quit(self):
		sys.exit()
	
	#overwrite event
	def closeEvent(self, event):
		self.hide()
		event.ignore()

		
	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	pyNotesApp = NotesMain()
	
	pyNotesApp.show()
	sys.exit(app.exec_())

