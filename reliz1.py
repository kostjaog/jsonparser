# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtGui import QIcon
from jsonschema import validate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import json
import Sql
import JSONSchema
import JsonSql
from functions import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 775)
        Form.setMinimumSize(QtCore.QSize(899, 555))
        self.treeViewer = QtWidgets.QTreeWidget(Form)
        self.treeViewer.setGeometry(QtCore.QRect(700, 10, 461, 331))
        self.treeViewer.setObjectName("treeViewer")
        self.treeViewer.headerItem().setText(0, "1")
        self.visB = QtWidgets.QPushButton(Form)
        self.visB.setGeometry(QtCore.QRect(490, 50, 181, 101))
        self.visB.setObjectName("visB")
        self.valViewer = QtWidgets.QTextBrowser(Form)
        self.valViewer.setGeometry(QtCore.QRect(480, 10, 201, 31))
        self.valViewer.setObjectName("valViewer")
        self.javacB = QtWidgets.QPushButton(Form)
        self.javacB.setGeometry(QtCore.QRect(490, 160, 181, 101))
        self.javacB.setObjectName("javacB")
        self.schemaTjsonB = QtWidgets.QPushButton(Form)
        self.schemaTjsonB.setGeometry(QtCore.QRect(490, 270, 181, 101))
        self.schemaTjsonB.setObjectName("schemaTjsonB")
        self.sqlB = QtWidgets.QPushButton(Form)
        self.sqlB.setGeometry(QtCore.QRect(490, 380, 181, 101))
        self.sqlB.setObjectName("sqlB")
        self.schemaViewer = QtWidgets.QTextBrowser(Form)
        self.schemaViewer.setGeometry(QtCore.QRect(10, 60, 461, 231))
        self.schemaViewer.setObjectName("schemaViewer")
        self.loadB = QtWidgets.QPushButton(Form)
        self.loadB.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.loadB.setObjectName("loadB")
        self.schemaedit = QtWidgets.QTextEdit(Form)
        self.schemaedit.setGeometry(QtCore.QRect(10, 450, 461, 321))
        self.schemaedit.setObjectName("schemaedit")
        self.valB = QtWidgets.QPushButton(Form)
        self.valB.setGeometry(QtCore.QRect(490, 720, 181, 51))
        self.valB.setObjectName("valB")
        self.sqlViewer = QtWidgets.QTextBrowser(Form)
        self.sqlViewer.setGeometry(QtCore.QRect(700, 350, 461, 421))
        self.sqlViewer.setObjectName("sqlViewer")
        self.schemaTjsonViewer = QtWidgets.QTextBrowser(Form)
        self.schemaTjsonViewer.setGeometry(QtCore.QRect(10, 300, 461, 141))
        self.schemaTjsonViewer.setObjectName("schemaTjsonViewer")
        self.dbTjsonB = QtWidgets.QPushButton(Form)
        self.dbTjsonB.setGeometry(QtCore.QRect(490, 560, 181, 51))
        self.dbTjsonB.setObjectName("dbTjsonB")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(490, 520, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(490, 650, 181, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 490, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(490, 620, 171, 16))
        self.label_2.setObjectName("label_2")
        self.schemaB = QtWidgets.QPushButton(Form)
        self.schemaB.setGeometry(QtCore.QRect(240, 10, 221, 41))
        self.schemaB.setObjectName("schemaB")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.visB.setText(_translate("Form", "Визуализировать"))
        self.javacB.setText(_translate("Form", "Генерация Java-класса"))
        self.schemaTjsonB.setText(_translate("Form", "JSON из JSON-schema"))
        self.sqlB.setText(_translate("Form", "SQL-запрос и загрузить в БД"))
        self.schemaViewer.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JSON-schema JSON файла:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.loadB.setText(_translate("Form", "Выбрать JSON файл"))
        self.schemaedit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JSON-schema:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.valB.setText(_translate("Form", "Валидация"))
        self.sqlViewer.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SQL-запрос:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.schemaTjsonViewer.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JSON из JSON-schema</p></body></html>"))
        self.dbTjsonB.setText(_translate("Form", "Выгрузить JSON"))
        self.label.setText(_translate("Form", "Введите название:"))
        self.label_2.setText(_translate("Form", "Введите название:"))
        self.schemaB.setText(_translate("Form", "JSON-schema"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadB.clicked.connect(self.load)
        self.ui.visB.clicked.connect(self.vis)
        self.ui.schemaB.clicked.connect(self.schema)
        self.ui.valB.clicked.connect(self.val)
        self.ui.javacB.clicked.connect(self.javac)
        self.ui.schemaTjsonB.clicked.connect(self.schemaTjson)
        self.error_dialog = QtWidgets.QErrorMessage()

    @pyqtSlot()
    def load(self):
        try:
            self.file = QtWidgets.QFileDialog.getOpenFileName()[0].replace('\\', '/')
            with open(self.file, 'r+') as f:
                self.js = f.read()
            self.jsl = json.loads(self.js)
        except:
            self.error_dialog.showMessage('Error. Celect json file or load another one')

    @pyqtSlot()
    def vis(self):
        try:
            fill_widget(self.ui.treeViewer, self.jsl)
        except:
            self.error_dialog.showMessage('Error')

    @pyqtSlot()
    def schema(self):
        try:
            schema = str(jsg.SchemaGenerator(self.jsl).to_dict())
            self.ui.schemaViewer.setText(schema)
        except:
            self.error_dialog.showMessage('Error')

    @pyqtSlot()
    def val(self):
        try:
            schema = self.ui.schemaedit.toPlainText()
            validateansw = validate(self.js, schema)
            self.ui.valViewer.setText(validateansw)
        except:
            self.error_dialog.showMessage('Error')

    @pyqtSlot()
    def javac(self):
        self.error_dialog.showMessage('Not working yet')

    @pyqtSlot()
    def schemaTjson(self):
        self.error_dialog.showMessage('Not working yet')


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Json-parser")
widget.setWindowIcon(QIcon("icon.png"))
widget.addWidget(mainWindow)
widget.setFixedHeight(780)
widget.setFixedWidth(1180)
widget.show()

sys.exit(app.exec_())