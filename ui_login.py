# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        styleLineEditOk = ("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(170, 170, 170);    \n"
"    color: rgb(50, 50, 50);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(50, 50, 50);\n"
"}")

        styleLineEditError = ("QLineEdit {\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(170, 170, 170);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")   
        
        stylePopUpError = ("background-color: rgb(170, 0, 0); border-radius: 10px;")
        stylePopUpOk = ("background-color: rgb(0, 255, 123); border-radius: 10px;") 
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 800)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icon/images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background-color: rgb(150, 150, 150);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.top_bar = QtWidgets.QFrame(self.centralwidget)
                self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
                self.top_bar.setStyleSheet("")
                self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.top_bar.setObjectName("top_bar")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
                self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.frame_error = QtWidgets.QFrame(self.top_bar)
                self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
                self.frame_error.setStyleSheet("background-color: rgb(170, 0, 0);\n"
        "border-radius: 10px;")
                self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_error.setObjectName("frame_error")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
                self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_error = QtWidgets.QLabel(self.frame_error)
                self.label_error.setAlignment(QtCore.Qt.AlignCenter)
                self.label_error.setObjectName("label_error")
                self.horizontalLayout_3.addWidget(self.label_error)
                self.pushButton_close = QtWidgets.QPushButton(self.frame_error)
                self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
                self.pushButton_close.setStyleSheet("QPushButton {\n"
        "    background-image: url(:/close_button/images/cil-x.png);\n"
        "    border-radius: 5px;\n"
        "    background-position: center;\n"
        "    background-color: rgb(120, 0, 0);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(130, 130, 130);\n"
        "    color: rgb(200, 200, 200);\n"
        "}")
                self.pushButton_close.setText("")
                self.pushButton_close.setObjectName("pushButton_close")
                self.horizontalLayout_3.addWidget(self.pushButton_close)
                self.horizontalLayout_2.addWidget(self.frame_error)
                self.verticalLayout.addWidget(self.top_bar)
                self.content = QtWidgets.QFrame(self.centralwidget)
                self.content.setStyleSheet("")
                self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.content.setFrameShadow(QtWidgets.QFrame.Raised)
                self.content.setObjectName("content")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.login_area = QtWidgets.QFrame(self.content)
                self.login_area.setMaximumSize(QtCore.QSize(450, 550))
                self.login_area.setStyleSheet("background-color: rgb(220, 220, 220);\n"
        "border-radius: 10px;")
                self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
                self.login_area.setObjectName("login_area")
                self.frame_logo = QtWidgets.QFrame(self.login_area)
                self.frame_logo.setGeometry(QtCore.QRect(55, 25, 345, 85))
                self.frame_logo.setStyleSheet("background-image: url(:/logo/images/logo.png);\n"
        "background-repeat: no-repeat;\n"
        "background-position: center;")
                self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_logo.setObjectName("frame_logo")
                self.frame_avatar = QtWidgets.QFrame(self.login_area)
                self.frame_avatar.setGeometry(QtCore.QRect(165, 110, 120, 120))
                self.frame_avatar.setStyleSheet("QFrame {\n"
        "background-image: url(:/avatar_logo/images/avatar.png);\n"
        "background-position: center;\n"
        "background-repeat: no-repeat;\n"
        "border-radius: 60px;\n"
        "}\n"
        "\n"
        "QFrame:hover {\n"
        "    border: 10px solid rgb(255, 225, 0);\n"
        "}")
                self.frame_avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_avatar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_avatar.setObjectName("frame_avatar")
                self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
                self.lineEdit_user.setGeometry(QtCore.QRect(85, 265, 280, 50))
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(10)
                self.lineEdit_user.setFont(font)
                self.lineEdit_user.setStyleSheet(self.styleLineEditOk)
                self.lineEdit_user.setText("")
                self.lineEdit_user.setMaxLength(32)
                self.lineEdit_user.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_user.setObjectName("lineEdit_user")
                self.lineEdit_pass = QtWidgets.QLineEdit(self.login_area)
                self.lineEdit_pass.setGeometry(QtCore.QRect(85, 325, 280, 50))
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(10)
                self.lineEdit_pass.setFont(font)
                self.lineEdit_pass.setStyleSheet(self.styleLineEditOk)
                self.lineEdit_pass.setText("")
                self.lineEdit_pass.setMaxLength(16)
                self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_pass.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_pass.setObjectName("lineEdit_pass")
                self.pushButton_enviar = QtWidgets.QPushButton(self.login_area)
                self.pushButton_enviar.setGeometry(QtCore.QRect(85, 430, 280, 50))
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_enviar.setFont(font)
                self.pushButton_enviar.setStyleSheet("QPushButton {\n"
        "    color: rgb(200, 200, 200);\n"
        "    background-color: rgb(100, 100, 100);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(50, 50, 50);\n"
        "    border: 2px solid rgb(70, 70, 70);\n"
        "    border-radius: 5px;\n"
        "    color: rgb(220, 220, 220);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(250, 230, 00);\n"
        "    border: 2px solid rgb(255, 165, 24);\n"
        "    color: rgb(50, 50, 50);\n"
        "}")
                self.pushButton_enviar.setObjectName("pushButton_enviar")
                self.horizontalLayout.addWidget(self.login_area)
                self.verticalLayout.addWidget(self.content)
                self.side_bar = QtWidgets.QFrame(self.centralwidget)
                self.side_bar.setMaximumSize(QtCore.QSize(16777215, 35))
                self.side_bar.setStyleSheet("")
                self.side_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.side_bar.setObjectName("side_bar")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_bar)
                self.verticalLayout_2.setContentsMargins(-1, -1, 15, -1)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.label_side = QtWidgets.QLabel(self.side_bar)
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.label_side.setFont(font)
                self.label_side.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.label_side.setObjectName("label_side")
                self.verticalLayout_2.addWidget(self.label_side)
                self.verticalLayout.addWidget(self.side_bar)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.pushButton_close.clicked.connect(lambda: self.frame_error.hide()) #FAZ SUMIR O FRAME DE ERRO QUANDO APERTA NO BOTÃO
                self.pushButton_close.clicked.connect(lambda: self.lineEdit_pass.setStyleSheet(self.styleLineEditOk))#FAZ SUMIR O ESTILO DE ERRO DA SENHA (BORDA VERMELHO) QUANDO APERTA NO BOTÃO
                self.pushButton_close.clicked.connect(lambda:self.lineEdit_user.setStyleSheet(self.styleLineEditOk))#FAZ SUMIR O ESTILO DE ERRO DO USER (BORDA VERMELHO) QUANDO APERTA NO BOTÃO
                
                ##FAZ O FRAME DE ERROR COMEÇAR OCULTO
                self.frame_error.hide()

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
                self.label_error.setText(_translate("MainWindow", "Error"))
                self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USUÁRIO"))
                self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "SENHA"))
                self.pushButton_enviar.setText(_translate("MainWindow", "ENVIAR"))
                self.label_side.setText(_translate("MainWindow", "Criado por: Arthur"))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())