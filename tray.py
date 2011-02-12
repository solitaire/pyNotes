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

import sys
from PyQt4 import QtCore, QtGui

class ApplicationTray:
    def __init__(self, parent):
        self.parent = parent
        self.tray = QtGui.QSystemTrayIcon(parent)
        trayMenu  = QtGui.QMenu(parent)
        
        self.exitAction = trayMenu.addAction("Close")
        self.newNoteAction = trayMenu.addAction("New note")
        
        self.tray.setContextMenu(trayMenu)
        
        self.tray.activated.connect(self.trayActivated)
        
        #context menu actions
        self.exitAction.triggered.connect(self.exit)
        self.newNoteAction.triggered.connect(self.createNote)


        self.tray.setIcon(QtGui.QIcon(":/icons/gnome-main-menu.svg"))
        self.tray.show() 
           
    @QtCore.pyqtSlot("QSystemTrayIcon::ActivationReason")
    def trayActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            if self.tray.isVisible():
                self.parent.show()
                self.tray.show()
            else:
                self.parent.show()
        else:
            pass
        
    def exit(self):
        sys.exit()
        
    def createNote(self):
        NotesMain.createNote(self.parent)