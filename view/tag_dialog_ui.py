# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tag_dialog.ui'
#
# Created: Fri Feb 11 23:01:46 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_tagform(object):
    def setupUi(self, tagform):
        tagform.setObjectName("tagform")
        tagform.resize(320, 120)
        self.verticalLayout = QtGui.QVBoxLayout(tagform)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtGui.QLabel(tagform)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoLabel = QtGui.QLabel(tagform)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout.addWidget(self.infoLabel)
        self.lineEdit = QtGui.QLineEdit(tagform)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(tagform)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(tagform)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), tagform.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), tagform.reject)
        QtCore.QMetaObject.connectSlotsByName(tagform)

    def retranslateUi(self, tagform):
        tagform.setWindowTitle(QtGui.QApplication.translate("tagform", "New tag", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("tagform", "New tag\'s name", None, QtGui.QApplication.UnicodeUTF8))
        self.infoLabel.setText(QtGui.QApplication.translate("tagform", "Name: ", None, QtGui.QApplication.UnicodeUTF8))

