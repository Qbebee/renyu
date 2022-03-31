from PyQt5 import QtCore,QtGui,QtWidgets
from ui import *
import sys 
class Ui_Dialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.formlayout = QtCore.QFormLayout()
        self.formlayout.addWidget(QtGui.QLabel("label_1"))
        
    
    formlayoutWidget = None
    formlayout = None
    label_1 = "姓名"
    label_2 = "翻堆日期"
    label_3 = "板数"
    label_4 = "散件数"
    lineEdit_1 = None
    lineEdit_2 = None
    lineEdit_3 = None
    lineEdit_4 = None
    def setupUi(self,Dialog):
       Dialog.setObjectName("Dialog")
       self.formlayoutWidget = QtWidgets.QWidget(Dialog)
       self.formlayoutWidget.setGeometry(QtCore.QRect(30,20,271,120))
       self.formlayoutWidget.setObjectName("formLayoutWidget")
       self.formlayout = QtWidgets.QFormLayout(self.formlayoutWidget)
       self.formlayout.setContentsMargins(0,0,0,0)
       self.formlayout.setObjectName("formLayout")
       self.label_1 = QtWidgets.QLabel(self.formlayoutWidget)
       self.label_1.setObjectName("label_1")
       self.formlayout.setWidget(0,QtWidgets.QFormLayout.LabelRole,self.label_1)
       self.lineEdit_1 = QtWidgets.QLineEdit(self.formlayoutWidget)
       self.lineEdit_1.setObjectName("lineEdit_1")
       self.formlayout.setWidget(0,QtWidgets.QFormLayout.FieldRole,self.lineEdit_1)
       self.label_2 = QtWidgets.QLabel(self.formlayoutWidget)
       self.label_2.setObjectName("label_2")
       self.formlayout.setWidget(1,QtWidgets.QFormLayout.LabelRole,self.label_2)
       self.lineEdit_2 = QtWidgets.QLineEdit(self.formlayoutWidget)
       self.lineEdit_2.setObjectName("lineEdit_1")
       self.formlayout.setWidget(1,QtWidgets.QFormLayout.FieldRole,self.lineEdit_2)
       self.label_3 = QtWidgets.QLabel(self.formlayoutWidget)
       self.label_3.setObjectName("label_3")
       self.formlayout.setWidget(2,QtWidgets.QFormLayout.LabelRole,self.label_3)
       self.lineEdit_3 = QtWidgets.QLineEdit(self.formlayoutWidget)
       self.lineEdit_3.setObjectName("lineEdit_1")
       self.formlayout.setWidget(2,QtWidgets.QFormLayout.FieldRole,self.lineEdit_3) 
       self.label_4 = QtWidgets.QLabel(self.formlayoutWidget)
       self.label_4.setObjectName("label_4")
       self.formlayout.setWidget(3,QtWidgets.QFormLayout.LabelRole,self.label_4)
       self.lineEdit_4 = QtWidgets.QLineEdit(self.formlayoutWidget)
       self.lineEdit_4.setObjectName("lineEdit_5")
       self.formlayout.setWidget(3,QtWidgets.QFormLayout.FieldRole,self.lineEdit_4)
       #self.label_5 = QtWidgets.QLabel(self.formlayoutWidget)
       #self.label_5.setObjectName("label_5")
       #self.formlayout.setWidget(4,QtWidgets.QFormLayout.LabelRole,self.label_5)
       #self.lineEdit_5 = QtWidgets.QLineEdit(self.formlayoutWidget)
       #self.lineEdit_5.setObjectName("lineEdit_5")
       #self.formlayout.setWidget(4,QtWidgets.QFormLayout.FieldRole,self.lineEdit_5)  
       self.retranslateUi(Dialog)
       QtCore.QMetaObject.connectSlotsByName(Dialog)
       
    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("翻堆数据录入表单","Dialog"))
        self.label_1.setText(_translate("Dialog","label_1"))
        self.label_2.setText(_translate("Dialog","label_2"))
        self.label_3.setText(_translate("Dialog","label_3"))
        self.label_4.setText(_translate("Dialog","label_4"))   
   ###     
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    
    #app.run(sys.argv)
    
    #app.show()
    sys.exit(app.exec_())
          