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
from view.notebook_dialog_ui import *

class NotebookDialog(QtGui.QDialog, Ui_notebookform):
    def __init__(self, parent=None, notebook_model=None):
        super(NotebookDialog, self).__init__(parent)
        self.notebook_model = notebook_model
        self.setupUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.rejected)
    
    def accepted(self):
        self.addNotebook()
        self.close()
    
    def rejected(self):
        self.close()
         
    def addNotebook(self):
        notebook = Notebook(name="%s" % (self.lineEdit.text()))
        row = self.notebook_model.rowCount()
        self.notebook_model.insertRows(row, notebook)
    