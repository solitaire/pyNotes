# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/notebook_dialog.ui'
#
# Created: Fri Feb 11 23:02:24 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_notebookform(object):
    def setupUi(self, notebookform):
        notebookform.setObjectName("notebookform")
        notebookform.resize(320, 120)
        self.verticalLayout = QtGui.QVBoxLayout(notebookform)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtGui.QLabel(notebookform)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoLabel = QtGui.QLabel(notebookform)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout.addWidget(self.infoLabel)
        self.lineEdit = QtGui.QLineEdit(notebookform)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(notebookform)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(notebookform)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), notebookform.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), notebookform.reject)
        QtCore.QMetaObject.connectSlotsByName(notebookform)

    def retranslateUi(self, notebookform):
        notebookform.setWindowTitle(QtGui.QApplication.translate("notebookform", "New notebook", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("notebookform", "New notebook\'s name", None, QtGui.QApplication.UnicodeUTF8))
        self.infoLabel.setText(QtGui.QApplication.translate("notebookform", "Name: ", None, QtGui.QApplication.UnicodeUTF8))

