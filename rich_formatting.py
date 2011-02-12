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

# Basic rich formatting class 
# Supports bold, italic and underlined text
# Text alignment and undo, redo, copy and paste methods

class RichFormatting:
    def __init__(self, ui):
        self.ui = ui
        self.connect_actions()
    
    def connect_actions(self):
        self.ui.boldButton.clicked.connect(self.text_bold)
        self.ui.italicButton.clicked.connect(self.text_italic)
        self.ui.underlineButton.clicked.connect(self.text_underline)
        
        QtCore.QObject.connect(self.ui.centerButton, QtCore.SIGNAL("clicked()"),
                                lambda format="center": self.text_align(format))
        QtCore.QObject.connect(self.ui.justifyButton, QtCore.SIGNAL("clicked()"),
                                lambda format="justify": self.text_align(format)) 
        QtCore.QObject.connect(self.ui.alignleftButton, QtCore.SIGNAL("clicked()"),
                                lambda format="left": self.text_align(format))
        QtCore.QObject.connect(self.ui.alignrightButton, QtCore.SIGNAL("clicked()"),
                                lambda format="right": self.text_align(format))
        
        QtCore.QObject.connect(self.ui.undoButton,  QtCore.SIGNAL("clicked()"), self.ui.notesTextEdit, QtCore.SLOT('undo()'))
        QtCore.QObject.connect(self.ui.redoButton,  QtCore.SIGNAL("clicked()"), self.ui.notesTextEdit, QtCore.SLOT('redo()'))
        QtCore.QObject.connect(self.ui.pasteButton, QtCore.SIGNAL("clicked()"), self.ui.notesTextEdit, QtCore.SLOT('paste()'))
        QtCore.QObject.connect(self.ui.cutButton,   QtCore.SIGNAL("clicked()"), self.ui.notesTextEdit, QtCore.SLOT('cut()'))

        
        self.__alignment_changed(self.ui.notesTextEdit.alignment())
    
    @QtCore.pyqtSlot()
    def text_bold(self):
        format = QtGui.QTextCharFormat()
        if self.ui.boldButton.isChecked():
            format.setFontWeight(QtGui.QFont.Bold)
        else:
            format.setFontWeight(QtGui.QFont.Normal)
        self.apply_on_selection(format)
        
    @QtCore.pyqtSlot()
    def text_italic(self):
        format = QtGui.QTextCharFormat()
        format.setFontItalic(self.ui.italicButton.isChecked())
        self.apply_on_selection(format)
        
    @QtCore.pyqtSlot()
    def text_underline(self):
        format = QtGui.QTextCharFormat()
        format.setFontUnderline(self.ui.underlineButton.isChecked())
        self.apply_on_selection(format)
        
    def text_align(self, format):
        if format == "left":
            self.ui.notesTextEdit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignAbsolute)
        elif format == "center":
            self.ui.notesTextEdit.setAlignment(QtCore.Qt.AlignHCenter)
        elif format == "right":
            self.ui.notesTextEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignAbsolute)
        elif format == "justify":
            self.ui.notesTextEdit.setAlignment(QtCore.Qt.AlignJustify)
            
    def __alignment_changed(self, state):
        if state == QtCore.Qt.AlignLeft:
            self.ui.alignleftButton.setChecked(True)
            self.ui.alignrightButton.setChecked(False)
            self.ui.centerButton.setChecked(False)
            self.ui.justifyButton.setChecked(False)
        elif state == QtCore.Qt.AlignHCenter:
            self.ui.alignleftButton.setChecked(False)
            self.ui.alignrightButton.setChecked(False)
            self.ui.centerButton.setChecked(True)
            self.ui.justifyButton.setChecked(False)
        elif state == QtCore.Qt.AlignJustify:
            self.ui.alignleftButton.setChecked(False)
            self.ui.alignrightButton.setChecked(False)
            self.ui.centerButton.setChecked(False)
            self.ui.justifyButton.setChecked(True)
        elif state == QtCore.Qt.AlignRight:
            self.ui.alignleftButton.setChecked(False)
            self.ui.alignrightButton.setChecked(True)
            self.ui.centerButton.setChecked(False)
            self.ui.justifyButton.setChecked(False)
        
    def apply_on_selection(self, format):
        cursor = self.ui.notesTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QtGui.QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.ui.notesTextEdit.mergeCurrentCharFormat(format)
        
