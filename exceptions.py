from PyQt5.QtWidgets import *

class NullValor(Exception):
    def msgError():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Aviso")
        msg.setText("Preencha todos os campos!")
        msg.exec_()