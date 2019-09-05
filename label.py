# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'label.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import cv2
import glob
import torch
import numpy as np
import tkinter as tk
from tkinter import filedialog
import torch.nn.functional as F
from torch.autograd import Variable
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 347)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 141, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 40, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.zhuanhua)
        self.pushButton.clicked.connect(self.daoru1)
        QtCore.QMetaObject.connectSlotsByName(Form)
       
    def daoru1(self):
        application_window = tk.Tk()
        # 设置文件对话框会显示的文件类型
        answer = filedialog.askdirectory(parent=application_window,
                                 initialdir=os.getcwd(),
                                 title="Please select a folder:")
        application_window.destroy()
        global k
        k=answer
    def zhuanhua(self):
        labeltext=self.lineEdit.text()
        z=k+"/*.jpg"
        listadd=glob.glob(z)
        with open("labels.txt","a") as f:
           for i in listadd:
               f.write(i)
               f.write(" ")
               f.write(labeltext)
               f.write("\n")
        f.close()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "深度学习图像分类标签器"))
        self.pushButton.setText(_translate("Form", "选择需打标签的文件夹"))
        self.label.setText(_translate("Form", "需要打上的标签名"))
        self.pushButton_2.setText(_translate("Form", "开始生成label的txt"))
if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 widget = QtWidgets.QWidget()
 ui = Ui_Form()
 ui.setupUi(widget)
 widget.show()
 sys.exit(app.exec_())
