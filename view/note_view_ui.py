# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/note_view.ui'
#
# Created: Sat Feb 12 13:51:10 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NoteEdit(object):
    def setupUi(self, NoteEdit):
        NoteEdit.setObjectName("NoteEdit")
        NoteEdit.resize(473, 300)
        self.gridLayout = QtGui.QGridLayout(NoteEdit)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleEdit = QtGui.QLineEdit(NoteEdit)
        self.titleEdit.setObjectName("titleEdit")
        self.horizontalLayout.addWidget(self.titleEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.notebooksBox = QtGui.QComboBox(NoteEdit)
        self.notebooksBox.setObjectName("notebooksBox")
        self.gridLayout.addWidget(self.notebooksBox, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exportToPdfButton = QtGui.QPushButton(NoteEdit)
        self.exportToPdfButton.setMaximumSize(QtCore.QSize(22, 22))
        self.exportToPdfButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/page_white_code_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportToPdfButton.setIcon(icon)
        self.exportToPdfButton.setIconSize(QtCore.QSize(24, 24))
        self.exportToPdfButton.setObjectName("exportToPdfButton")
        self.horizontalLayout_4.addWidget(self.exportToPdfButton)
        self.exportToPlainTextButton = QtGui.QPushButton(NoteEdit)
        self.exportToPlainTextButton.setMaximumSize(QtCore.QSize(22, 22))
        self.exportToPlainTextButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/page_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportToPlainTextButton.setIcon(icon1)
        self.exportToPlainTextButton.setIconSize(QtCore.QSize(24, 24))
        self.exportToPlainTextButton.setObjectName("exportToPlainTextButton")
        self.horizontalLayout_4.addWidget(self.exportToPlainTextButton)
        self.exportToHtmlButton = QtGui.QPushButton(NoteEdit)
        self.exportToHtmlButton.setMaximumSize(QtCore.QSize(22, 22))
        self.exportToHtmlButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/page_world.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportToHtmlButton.setIcon(icon2)
        self.exportToHtmlButton.setIconSize(QtCore.QSize(24, 24))
        self.exportToHtmlButton.setObjectName("exportToHtmlButton")
        self.horizontalLayout_4.addWidget(self.exportToHtmlButton)
        self.snippetButton = QtGui.QPushButton(NoteEdit)
        self.snippetButton.setMaximumSize(QtCore.QSize(22, 22))
        self.snippetButton.setText("")
        self.snippetButton.setIcon(icon)
        self.snippetButton.setObjectName("snippetButton")
        self.horizontalLayout_4.addWidget(self.snippetButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(NoteEdit)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.notesTags = QtGui.QLineEdit(NoteEdit)
        self.notesTags.setObjectName("notesTags")
        self.horizontalLayout_3.addWidget(self.notesTags)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.undoButton = QtGui.QPushButton(NoteEdit)
        self.undoButton.setMinimumSize(QtCore.QSize(22, 22))
        self.undoButton.setMaximumSize(QtCore.QSize(22, 22))
        self.undoButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/arrow_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon3)
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout_2.addWidget(self.undoButton)
        self.redoButton = QtGui.QPushButton(NoteEdit)
        self.redoButton.setMinimumSize(QtCore.QSize(22, 22))
        self.redoButton.setMaximumSize(QtCore.QSize(22, 22))
        self.redoButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/arrow_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon4)
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout_2.addWidget(self.redoButton)
        self.pasteButton = QtGui.QPushButton(NoteEdit)
        self.pasteButton.setMinimumSize(QtCore.QSize(22, 22))
        self.pasteButton.setMaximumSize(QtCore.QSize(22, 22))
        self.pasteButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/paste_plain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pasteButton.setIcon(icon5)
        self.pasteButton.setObjectName("pasteButton")
        self.horizontalLayout_2.addWidget(self.pasteButton)
        self.cutButton = QtGui.QPushButton(NoteEdit)
        self.cutButton.setMinimumSize(QtCore.QSize(22, 22))
        self.cutButton.setMaximumSize(QtCore.QSize(22, 22))
        self.cutButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cutButton.setIcon(icon6)
        self.cutButton.setObjectName("cutButton")
        self.horizontalLayout_2.addWidget(self.cutButton)
        self.boldButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boldButton.sizePolicy().hasHeightForWidth())
        self.boldButton.setSizePolicy(sizePolicy)
        self.boldButton.setMaximumSize(QtCore.QSize(22, 22))
        self.boldButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/text_bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boldButton.setIcon(icon7)
        self.boldButton.setCheckable(True)
        self.boldButton.setAutoDefault(False)
        self.boldButton.setDefault(False)
        self.boldButton.setFlat(False)
        self.boldButton.setObjectName("boldButton")
        self.horizontalLayout_2.addWidget(self.boldButton)
        self.italicButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.italicButton.sizePolicy().hasHeightForWidth())
        self.italicButton.setSizePolicy(sizePolicy)
        self.italicButton.setMaximumSize(QtCore.QSize(22, 22))
        self.italicButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/text_italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italicButton.setIcon(icon8)
        self.italicButton.setCheckable(True)
        self.italicButton.setAutoDefault(False)
        self.italicButton.setDefault(False)
        self.italicButton.setFlat(False)
        self.italicButton.setObjectName("italicButton")
        self.horizontalLayout_2.addWidget(self.italicButton)
        self.underlineButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.underlineButton.sizePolicy().hasHeightForWidth())
        self.underlineButton.setSizePolicy(sizePolicy)
        self.underlineButton.setMaximumSize(QtCore.QSize(22, 22))
        self.underlineButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/text_underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underlineButton.setIcon(icon9)
        self.underlineButton.setCheckable(True)
        self.underlineButton.setAutoDefault(False)
        self.underlineButton.setDefault(False)
        self.underlineButton.setFlat(False)
        self.underlineButton.setObjectName("underlineButton")
        self.horizontalLayout_2.addWidget(self.underlineButton)
        self.alignleftButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignleftButton.sizePolicy().hasHeightForWidth())
        self.alignleftButton.setSizePolicy(sizePolicy)
        self.alignleftButton.setMaximumSize(QtCore.QSize(22, 22))
        self.alignleftButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/text_align_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignleftButton.setIcon(icon10)
        self.alignleftButton.setCheckable(True)
        self.alignleftButton.setAutoDefault(False)
        self.alignleftButton.setDefault(False)
        self.alignleftButton.setFlat(False)
        self.alignleftButton.setObjectName("alignleftButton")
        self.horizontalLayout_2.addWidget(self.alignleftButton)
        self.centerButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerButton.sizePolicy().hasHeightForWidth())
        self.centerButton.setSizePolicy(sizePolicy)
        self.centerButton.setMaximumSize(QtCore.QSize(22, 22))
        self.centerButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/text_align_center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centerButton.setIcon(icon11)
        self.centerButton.setCheckable(True)
        self.centerButton.setAutoDefault(False)
        self.centerButton.setDefault(False)
        self.centerButton.setFlat(False)
        self.centerButton.setObjectName("centerButton")
        self.horizontalLayout_2.addWidget(self.centerButton)
        self.alignrightButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignrightButton.sizePolicy().hasHeightForWidth())
        self.alignrightButton.setSizePolicy(sizePolicy)
        self.alignrightButton.setMaximumSize(QtCore.QSize(22, 22))
        self.alignrightButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/text_align_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignrightButton.setIcon(icon12)
        self.alignrightButton.setCheckable(True)
        self.alignrightButton.setAutoDefault(False)
        self.alignrightButton.setDefault(False)
        self.alignrightButton.setFlat(False)
        self.alignrightButton.setObjectName("alignrightButton")
        self.horizontalLayout_2.addWidget(self.alignrightButton)
        self.justifyButton = QtGui.QPushButton(NoteEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.justifyButton.sizePolicy().hasHeightForWidth())
        self.justifyButton.setSizePolicy(sizePolicy)
        self.justifyButton.setMaximumSize(QtCore.QSize(22, 22))
        self.justifyButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/text_align_justify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.justifyButton.setIcon(icon13)
        self.justifyButton.setCheckable(True)
        self.justifyButton.setAutoDefault(False)
        self.justifyButton.setDefault(False)
        self.justifyButton.setFlat(False)
        self.justifyButton.setObjectName("justifyButton")
        self.horizontalLayout_2.addWidget(self.justifyButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.notesTextEdit = QtGui.QTextEdit(NoteEdit)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridLayout.addWidget(self.notesTextEdit, 3, 0, 1, 2)

        self.retranslateUi(NoteEdit)
        QtCore.QMetaObject.connectSlotsByName(NoteEdit)

    def retranslateUi(self, NoteEdit):
        NoteEdit.setWindowTitle(QtGui.QApplication.translate("NoteEdit", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NoteEdit", "Tags", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
