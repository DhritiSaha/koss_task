# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'length.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(272, 467)
        self.input = QtGui.QLineEdit(Form)
        self.input.setGeometry(QtCore.QRect(10, 20, 113, 22))
        self.input.setObjectName(_fromUtf8("input"))
        self.output = QtGui.QLineEdit(Form)
        self.output.setGeometry(QtCore.QRect(10, 210, 113, 22))
        self.output.setObjectName(_fromUtf8("output"))
        self.to = QtGui.QComboBox(Form)
        self.to.setGeometry(QtCore.QRect(10, 250, 73, 22))
        self.to.setObjectName(_fromUtf8("to"))
        self.frm = QtGui.QComboBox(Form)
        self.frm.setGeometry(QtCore.QRect(10, 60, 73, 22))
        self.frm.setObjectName(_fromUtf8("frm"))
        self.three = QtGui.QPushButton(Form)
        self.three.setGeometry(QtCore.QRect(150, 100, 93, 28))
        self.three.setObjectName(_fromUtf8("three"))
        self.seven = QtGui.QPushButton(Form)
        self.seven.setGeometry(QtCore.QRect(150, 260, 93, 28))
        self.seven.setObjectName(_fromUtf8("seven"))
        self.six = QtGui.QPushButton(Form)
        self.six.setGeometry(QtCore.QRect(150, 220, 93, 28))
        self.six.setObjectName(_fromUtf8("six"))
        self.one = QtGui.QPushButton(Form)
        self.one.setGeometry(QtCore.QRect(150, 20, 93, 28))
        self.one.setObjectName(_fromUtf8("one"))
        self.two = QtGui.QPushButton(Form)
        self.two.setGeometry(QtCore.QRect(150, 60, 93, 28))
        self.two.setObjectName(_fromUtf8("two"))
        self.five = QtGui.QPushButton(Form)
        self.five.setGeometry(QtCore.QRect(150, 180, 93, 28))
        self.five.setObjectName(_fromUtf8("five"))
        self.four = QtGui.QPushButton(Form)
        self.four.setGeometry(QtCore.QRect(150, 140, 93, 28))
        self.four.setObjectName(_fromUtf8("four"))
        self.nine = QtGui.QPushButton(Form)
        self.nine.setGeometry(QtCore.QRect(150, 340, 93, 28))
        self.nine.setObjectName(_fromUtf8("nine"))
        self.eight = QtGui.QPushButton(Form)
        self.eight.setGeometry(QtCore.QRect(150, 300, 93, 28))
        self.eight.setObjectName(_fromUtf8("eight"))
        self.zero = QtGui.QPushButton(Form)
        self.zero.setGeometry(QtCore.QRect(150, 380, 93, 28))
        self.zero.setObjectName(_fromUtf8("zero"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 420, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LENGTH", None))
        Form.setWindowIcon(QtGui.QIcon('kosslogo.png'))
        
        self.three.setText(_translate("Form", "3", None))
        self.seven.setText(_translate("Form", "7", None))
        self.six.setText(_translate("Form", "6", None))
        self.one.setText(_translate("Form", "1", None))
        self.two.setText(_translate("Form", "2", None))
        self.five.setText(_translate("Form", "5", None))
        self.four.setText(_translate("Form", "4", None))
        self.nine.setText(_translate("Form", "9", None))
        self.eight.setText(_translate("Form", "8", None))
        self.zero.setText(_translate("Form", "0", None))
        self.pushButton.setText(_translate("Form", ".", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

