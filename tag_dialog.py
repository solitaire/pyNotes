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

from PyQt4 import QtCore, QtGui
from model.tag import *
from view.tag_dialog_ui import *

class TagDialog(QtGui.QDialog, Ui_tagform):
    def __init__(self, parent=None, tag_model=None):
        super(TagDialog, self).__init__(parent)
        self.tag_model = tag_model
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)
    
    @QtCore.pyqtSlot()
    def accepted(self):
        self.addTag()
        self.close()
    
    @QtCore.pyqtSlot()
    def rejected(self):
        self.close()
        
    
    def addTag(self):
        tag_name = "%s" % (self.lineEdit.text())
        tag_name = tag_name.strip()
        tag = Tag(name=tag_name)
        row = self.tag_model.rowCount()
        self.tag_model.insertRows(row, tag)