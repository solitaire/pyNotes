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

# Universal exporter class for multiple output formats
# Designed for pdf export, but can be easily customizable for any other format
# Future plans: xml ad odf format
     
class Exporter(QtCore.QObject):
    def __init__(self, parent, editor):
        self.parent = parent
        self.editor = editor
        
    def file_browser(self):
        file_dialog = QtGui.QFileDialog(self.parent)
        self.filename = file_dialog.getSaveFileName()
        
    def export(self,output_format=None):
        self.file_browser()
 
class PdfExporter(Exporter):
    def __init__(self, parent, editor, page_size):
        super(PdfExporter, self).__init__(parent, editor)
        self.page_size = page_size
        
    def export(self, output_format):
        self.file_browser()
        printer = QtGui.QPrinter()
        printer.setPageSize(self.page_size)
        printer.setOutputFormat(output_format)
        printer.setOutputFileName(self.filename)
        if not self.filename.isEmpty():
            self.editor.print_(printer)        
        
class HtmlExporter(Exporter):
    def __init__(self, parent, editor):
        super(HtmlExporter,self).__init__(parent, editor)
        
    def export(self, output_format=None):
        self.file_browser()
        content = self.editor.toHtml()
        
        if not self.filename.isEmpty():
            with open(self.filename, 'w') as file:
                file.write(content)

class PlainTextExporter(Exporter):
    def __init__(self, parent, editor):
        super(PlainTextExporter,self).__init__(parent, editor)
        
    def export(self, output_format=None):
        self.file_browser()
        content = self.editor.toPlainText()
        if not self.filename.isEmpty():
            with open(self.filename, 'w') as file:
                file.write(content)
            
            

#Simple wrapper            
class NoteExporter():
    def __init__(self, parent, ui):
        self.parent = parent
        self.ui = ui
        self.ui.exportToPdfButton.clicked.connect(self.exportToPdf)
        self.ui.exportToHtmlButton.clicked.connect(self.exportToHTML)
        self.ui.exportToPlainTextButton.clicked.connect(self.exportToPlainText)
       
    @QtCore.pyqtSlot() 
    def exportToPdf(self):
        pdfExporter = PdfExporter(self.parent, self.ui.notesTextEdit, QtGui.QPrinter.A4)
        pdfExporter.export(QtGui.QPrinter.PdfFormat)
        print(self.ui.notesTextEdit.toPlainText())
        
    @QtCore.pyqtSlot()  
    def exportToHTML(self):
        htmlExporter = HtmlExporter(self.parent, self.ui.notesTextEdit)
        htmlExporter.export()
    
    @QtCore.pyqtSlot()   
    def exportToPlainText(self):
        plainExporter = PlainTextExporter(self.parent, self.ui.notesTextEdit)
        plainExporter.export()    

        