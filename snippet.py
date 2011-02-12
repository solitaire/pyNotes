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
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_all_lexers
from pygments.formatters import HtmlFormatter
from view.snippet_dialog_ui import *


class SnippetDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent, text_edit):
        super(SnippetDialog, self).__init__(parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.rejected)
        self.text_edit = text_edit
        self.__insert_langs()
          
    def accepted(self):
        result = self.__pygmentize("%s" % (self.textEdit.toPlainText()))
        self.text_edit.append(result)
        self.text_edit.insertPlainText('\n')
        
    def rejected(self):
        self.close()
        
    def __insert_langs(self):
        for lang in get_all_lexers():
            self.comboBox.insertItem(1, lang[0])
        
    def __pygmentize(self, text):
        lexer_name = "%s" % (self.comboBox.currentText())
        lexer = get_lexer_by_name(lexer_name.lower(), stripall=True)
        formatter = HtmlFormatter()
        formatter.noclasses = True
        return highlight(text, lexer, formatter)
    
    

    




        

                    