# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/notes.ui'
#
# Created: Sat Feb 12 01:19:54 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Notebook(object):
    def setupUi(self, Notebook):
        Notebook.setObjectName("Notebook")
        Notebook.resize(800, 600)
        Notebook.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/gnome-main-menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Notebook.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Notebook)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(300, 300))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtGui.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchField = QtGui.QLineEdit(self.widget)
        self.searchField.setObjectName("searchField")
        self.horizontalLayout.addWidget(self.searchField)
        self.searchButton = QtGui.QPushButton(self.widget)
        self.searchButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QtCore.QSize(22, 22))
        self.searchButton.setFlat(True)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.notes = QtGui.QTreeView(self.widget)
        self.notes.setMinimumSize(QtCore.QSize(0, 120))
        self.notes.setMaximumSize(QtCore.QSize(16777215, 150))
        self.notes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.notes.setRootIsDecorated(False)
        self.notes.setItemsExpandable(False)
        self.notes.setExpandsOnDoubleClick(False)
        self.notes.setObjectName("notes")
        self.notes.header().setVisible(False)
        self.gridLayout_4.addWidget(self.notes, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.titleEdit = QtGui.QLineEdit(self.widget)
        self.titleEdit.setObjectName("titleEdit")
        self.horizontalLayout_3.addWidget(self.titleEdit)
        self.notebooksBox = QtGui.QComboBox(self.widget)
        self.notebooksBox.setObjectName("notebooksBox")
        self.horizontalLayout_3.addWidget(self.notebooksBox)
        self.removeNoteFromNotebookButton = QtGui.QPushButton(self.widget)
        self.removeNoteFromNotebookButton.setMaximumSize(QtCore.QSize(22, 22))
        self.removeNoteFromNotebookButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeNoteFromNotebookButton.setIcon(icon2)
        self.removeNoteFromNotebookButton.setObjectName("removeNoteFromNotebookButton")
        self.horizontalLayout_3.addWidget(self.removeNoteFromNotebookButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.exportToPdfButton = QtGui.QPushButton(self.widget)
        self.exportToPdfButton.setMaximumSize(QtCore.QSize(22, 22))
        self.exportToPdfButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/page_white_acrobat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportToPdfButton.setIcon(icon3)
        self.exportToPdfButton.setIconSize(QtCore.QSize(24, 24))
        self.exportToPdfButton.setObjectName("exportToPdfButton")
        self.gridLayout_3.addWidget(self.exportToPdfButton, 0, 1, 1, 1)
        self.exportToPlainTextButton = QtGui.QPushButton(self.widget)
        self.exportToPlainTextButton.setMaximumSize(QtCore.QSize(22, 22))
        self.exportToPlainTextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/page_white_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportToPlainTextButton.setIcon(icon4)
        self.exportToPlainTextButton.setIconSize(QtCore.QSize(24, 24))
        self.exportToPlainTextButton.setObjectName("exportToPlainTextButton")
        self.gridLayout_3.addWidget(self.exportToPlainTextButton, 0, 3, 1, 1)
        self.exportToHtmlButton = QtGui.QPushButton(self.widget)
        self.exportToHtmlButton.setMaximumSize(QtCore.QSize(22, 22))
        self.exportToHtmlButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/page_world.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportToHtmlButton.setIcon(icon5)
        self.exportToHtmlButton.setIconSize(QtCore.QSize(24, 24))
        self.exportToHtmlButton.setObjectName("exportToHtmlButton")
        self.gridLayout_3.addWidget(self.exportToHtmlButton, 0, 4, 1, 1)
        self.snippetButton = QtGui.QPushButton(self.widget)
        self.snippetButton.setMaximumSize(QtCore.QSize(22, 22))
        self.snippetButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/page_white_code_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snippetButton.setIcon(icon6)
        self.snippetButton.setObjectName("snippetButton")
        self.gridLayout_3.addWidget(self.snippetButton, 0, 5, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 6, 1, 1)
        self.notesTags = QtGui.QLineEdit(self.widget)
        self.notesTags.setObjectName("notesTags")
        self.gridLayout_3.addWidget(self.notesTags, 0, 7, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.undoButton = QtGui.QPushButton(self.widget)
        self.undoButton.setMinimumSize(QtCore.QSize(22, 22))
        self.undoButton.setMaximumSize(QtCore.QSize(22, 22))
        self.undoButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/arrow_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon7)
        self.undoButton.setObjectName("undoButton")
        self.gridLayout_2.addWidget(self.undoButton, 0, 0, 1, 1)
        self.redoButton = QtGui.QPushButton(self.widget)
        self.redoButton.setMinimumSize(QtCore.QSize(22, 22))
        self.redoButton.setMaximumSize(QtCore.QSize(22, 22))
        self.redoButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/arrow_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon8)
        self.redoButton.setObjectName("redoButton")
        self.gridLayout_2.addWidget(self.redoButton, 0, 1, 1, 1)
        self.pasteButton = QtGui.QPushButton(self.widget)
        self.pasteButton.setMinimumSize(QtCore.QSize(22, 22))
        self.pasteButton.setMaximumSize(QtCore.QSize(22, 22))
        self.pasteButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/paste_plain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pasteButton.setIcon(icon9)
        self.pasteButton.setObjectName("pasteButton")
        self.gridLayout_2.addWidget(self.pasteButton, 0, 2, 1, 1)
        self.cutButton = QtGui.QPushButton(self.widget)
        self.cutButton.setMinimumSize(QtCore.QSize(22, 22))
        self.cutButton.setMaximumSize(QtCore.QSize(22, 22))
        self.cutButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cutButton.setIcon(icon10)
        self.cutButton.setObjectName("cutButton")
        self.gridLayout_2.addWidget(self.cutButton, 0, 3, 1, 1)
        self.boldButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boldButton.sizePolicy().hasHeightForWidth())
        self.boldButton.setSizePolicy(sizePolicy)
        self.boldButton.setMinimumSize(QtCore.QSize(22, 22))
        self.boldButton.setMaximumSize(QtCore.QSize(22, 22))
        self.boldButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/text_bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boldButton.setIcon(icon11)
        self.boldButton.setCheckable(True)
        self.boldButton.setAutoDefault(False)
        self.boldButton.setDefault(False)
        self.boldButton.setFlat(False)
        self.boldButton.setObjectName("boldButton")
        self.gridLayout_2.addWidget(self.boldButton, 0, 4, 1, 1)
        self.italicButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.italicButton.sizePolicy().hasHeightForWidth())
        self.italicButton.setSizePolicy(sizePolicy)
        self.italicButton.setMinimumSize(QtCore.QSize(22, 22))
        self.italicButton.setMaximumSize(QtCore.QSize(22, 22))
        self.italicButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/text_italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italicButton.setIcon(icon12)
        self.italicButton.setCheckable(True)
        self.italicButton.setAutoDefault(False)
        self.italicButton.setDefault(False)
        self.italicButton.setFlat(False)
        self.italicButton.setObjectName("italicButton")
        self.gridLayout_2.addWidget(self.italicButton, 0, 5, 1, 1)
        self.underlineButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.underlineButton.sizePolicy().hasHeightForWidth())
        self.underlineButton.setSizePolicy(sizePolicy)
        self.underlineButton.setMinimumSize(QtCore.QSize(22, 22))
        self.underlineButton.setMaximumSize(QtCore.QSize(22, 22))
        self.underlineButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/text_underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underlineButton.setIcon(icon13)
        self.underlineButton.setCheckable(True)
        self.underlineButton.setAutoDefault(False)
        self.underlineButton.setDefault(False)
        self.underlineButton.setFlat(False)
        self.underlineButton.setObjectName("underlineButton")
        self.gridLayout_2.addWidget(self.underlineButton, 0, 6, 1, 1)
        self.alignleftButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignleftButton.sizePolicy().hasHeightForWidth())
        self.alignleftButton.setSizePolicy(sizePolicy)
        self.alignleftButton.setMinimumSize(QtCore.QSize(22, 22))
        self.alignleftButton.setMaximumSize(QtCore.QSize(22, 22))
        self.alignleftButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/text_align_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignleftButton.setIcon(icon14)
        self.alignleftButton.setCheckable(True)
        self.alignleftButton.setAutoDefault(False)
        self.alignleftButton.setDefault(False)
        self.alignleftButton.setFlat(False)
        self.alignleftButton.setObjectName("alignleftButton")
        self.gridLayout_2.addWidget(self.alignleftButton, 0, 7, 1, 1)
        self.centerButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerButton.sizePolicy().hasHeightForWidth())
        self.centerButton.setSizePolicy(sizePolicy)
        self.centerButton.setMinimumSize(QtCore.QSize(22, 22))
        self.centerButton.setMaximumSize(QtCore.QSize(22, 22))
        self.centerButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/text_align_center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centerButton.setIcon(icon15)
        self.centerButton.setCheckable(True)
        self.centerButton.setAutoDefault(False)
        self.centerButton.setDefault(False)
        self.centerButton.setFlat(False)
        self.centerButton.setObjectName("centerButton")
        self.gridLayout_2.addWidget(self.centerButton, 0, 8, 1, 1)
        self.alignrightButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignrightButton.sizePolicy().hasHeightForWidth())
        self.alignrightButton.setSizePolicy(sizePolicy)
        self.alignrightButton.setMinimumSize(QtCore.QSize(22, 22))
        self.alignrightButton.setMaximumSize(QtCore.QSize(22, 22))
        self.alignrightButton.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/text_align_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignrightButton.setIcon(icon16)
        self.alignrightButton.setCheckable(True)
        self.alignrightButton.setAutoDefault(False)
        self.alignrightButton.setDefault(False)
        self.alignrightButton.setFlat(False)
        self.alignrightButton.setObjectName("alignrightButton")
        self.gridLayout_2.addWidget(self.alignrightButton, 0, 9, 1, 1)
        self.justifyButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.justifyButton.sizePolicy().hasHeightForWidth())
        self.justifyButton.setSizePolicy(sizePolicy)
        self.justifyButton.setMinimumSize(QtCore.QSize(22, 22))
        self.justifyButton.setMaximumSize(QtCore.QSize(22, 22))
        self.justifyButton.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/text_align_justify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.justifyButton.setIcon(icon17)
        self.justifyButton.setCheckable(True)
        self.justifyButton.setAutoDefault(False)
        self.justifyButton.setDefault(False)
        self.justifyButton.setFlat(False)
        self.justifyButton.setObjectName("justifyButton")
        self.gridLayout_2.addWidget(self.justifyButton, 0, 10, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(171, 29, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 4, 1, 1, 1)
        self.notesTextEdit = QtGui.QTextEdit(self.widget)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridLayout_4.addWidget(self.notesTextEdit, 5, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        Notebook.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Notebook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Notebook.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Notebook)
        self.statusbar.setObjectName("statusbar")
        Notebook.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(Notebook)
        self.dockWidget.setMinimumSize(QtCore.QSize(209, 217))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.notebooksContents = QtGui.QWidget()
        self.notebooksContents.setObjectName("notebooksContents")
        self.gridLayout_5 = QtGui.QGridLayout(self.notebooksContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.all_notes = QtGui.QCommandLinkButton(self.notebooksContents)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.all_notes.setIcon(icon18)
        self.all_notes.setObjectName("all_notes")
        self.gridLayout_5.addWidget(self.all_notes, 0, 0, 1, 1)
        self.uncategorized_notes = QtGui.QCommandLinkButton(self.notebooksContents)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/folder_page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uncategorized_notes.setIcon(icon19)
        self.uncategorized_notes.setObjectName("uncategorized_notes")
        self.gridLayout_5.addWidget(self.uncategorized_notes, 1, 0, 1, 1)
        self.notebooks = QtGui.QListView(self.notebooksContents)
        self.notebooks.setObjectName("notebooks")
        self.gridLayout_5.addWidget(self.notebooks, 2, 0, 1, 1)
        self.dockWidget.setWidget(self.notebooksContents)
        Notebook.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.toolBar = QtGui.QToolBar(Notebook)
        self.toolBar.setObjectName("toolBar")
        Notebook.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.dockWidget_2 = QtGui.QDockWidget(Notebook)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tags = QtGui.QListView(self.dockWidgetContents)
        self.tags.setObjectName("tags")
        self.gridLayout_6.addWidget(self.tags, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents)
        Notebook.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.action_new_note = QtGui.QAction(Notebook)
        self.action_new_note.setIcon(icon4)
        self.action_new_note.setIconVisibleInMenu(True)
        self.action_new_note.setObjectName("action_new_note")
        self.action_new_notebook = QtGui.QAction(Notebook)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/book_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_notebook.setIcon(icon20)
        self.action_new_notebook.setIconVisibleInMenu(True)
        self.action_new_notebook.setObjectName("action_new_notebook")
        self.action_close = QtGui.QAction(Notebook)
        self.action_close.setCheckable(False)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/door_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon21)
        self.action_close.setIconVisibleInMenu(True)
        self.action_close.setObjectName("action_close")
        self.actionNew_tag = QtGui.QAction(Notebook)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/tag_blue_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_tag.setIcon(icon22)
        self.actionNew_tag.setIconVisibleInMenu(True)
        self.actionNew_tag.setObjectName("actionNew_tag")
        self.menuFile.addAction(self.action_new_note)
        self.menuFile.addAction(self.action_new_notebook)
        self.menuFile.addAction(self.actionNew_tag)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_close)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.action_new_note)
        self.toolBar.addAction(self.action_new_notebook)
        self.toolBar.addAction(self.actionNew_tag)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_close)

        self.retranslateUi(Notebook)
        QtCore.QMetaObject.connectSlotsByName(Notebook)

    def retranslateUi(self, Notebook):
        Notebook.setWindowTitle(QtGui.QApplication.translate("Notebook", "pyNotes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Notebook", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Notebook", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.all_notes.setText(QtGui.QApplication.translate("Notebook", "All Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.uncategorized_notes.setText(QtGui.QApplication.translate("Notebook", "Uncategorized notes", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Notebook", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new_note.setText(QtGui.QApplication.translate("Notebook", "New note", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new_note.setShortcut(QtGui.QApplication.translate("Notebook", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new_notebook.setText(QtGui.QApplication.translate("Notebook", "New notebook", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new_notebook.setShortcut(QtGui.QApplication.translate("Notebook", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.action_close.setText(QtGui.QApplication.translate("Notebook", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.action_close.setShortcut(QtGui.QApplication.translate("Notebook", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_tag.setText(QtGui.QApplication.translate("Notebook", "New tag", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_tag.setShortcut(QtGui.QApplication.translate("Notebook", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
