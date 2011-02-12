# -*- coding: utf-8 -*-
#
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

from note_mapper import *
from view.note_view_ui import Ui_NoteEdit
from model import *
from rich_formatting import *
from exporter import *

class NoteForm(QtGui.QDialog):
    def __init__(self, parent, notes_model, notebooks_model, index):
        super(NoteForm, self).__init__(parent)
        self.notes_model = notes_model
        self.notebooks_model = notebooks_model
        self.ui= Ui_NoteEdit()
        self.ui.setupUi(self)
        self.ui.notebooksBox.setModel(self.notebooks_model)    
        self.widgets = [self.ui.notesTextEdit, self.ui.titleEdit, self.ui.notebooksBox, self.ui.notesTags]
        self.createMapper(index)
        self.rich_edit = RichFormatting(self.ui)
        self.note_exporter = NoteExporter(self, self.ui)
        
    def createMapper(self, index):
        self.mapper = NoteMapper(self, self.notes_model, self.widgets)
        self.mapper.setCurrentIndex(index.row())
        
