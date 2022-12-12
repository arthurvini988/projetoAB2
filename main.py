#imports
from PyQt5.QtWidgets import *
from ui_login import *
from ui_estoque import *
from database import DataBase
from produtos import *
from exceptions import *
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

#classes
class Login (QMainWindow):
    def checkLogin (self):
        self.users = DataBase()
        self.users.conectar()
        autenticado = self.users.check_user(self.ui.lineEdit_user.text().upper(), self.ui.lineEdit_pass.text())
        textUser = ""
        textPass = ""

        def showMessage(message):
            self.ui.frame_error.show()
            self.ui.label_error.setText (message)

        #CHECK USER
        if not self.ui.lineEdit_user.text():
            userError = " Usuário vazio! "
            self.ui.lineEdit_user.setStyleSheet(self.ui.styleLineEditError)
        else:
            userError = ""
            self.ui.lineEdit_user.setStyleSheet(self.ui.styleLineEditOk)
        
        #CHECK SENHA
        if not self.ui.lineEdit_pass.text():
            passError = " Senha vazia! "
            self.ui.lineEdit_pass.setStyleSheet(self.ui.styleLineEditError)
        else:
            passError = ""
            self.ui.lineEdit_pass.setStyleSheet(self.ui.styleLineEditOk)

        #CHECK FIELDS
        if userError + passError != '':
            text = userError+passError
            showMessage (text)
            self.ui.frame_error.setStyleSheet(self.ui.stylePopUpError)
        
        ##LOGIN
        elif (autenticado==True):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Aviso")
            msg.setText("Login realizado com sucesso!")
            msg.exec_()
            self.trocaWindow()
        
        else:
            text = "Dados incorretos!"
            showMessage(text)
            self.ui.frame_error.setStyleSheet(self.ui.stylePopUpError)
         

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.estoque = Estoque()
        self.ui.pushButton_enviar.clicked.connect(self.checkLogin)

    def trocaWindow (self):
        self.estoque.show()
        self.close()

class Estoque (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_Estoque()
        self.xd = Ui_MainWindow()
        self.ui.setupUi(self)  


        ##BOTÕES DO SISTEMA
        self.ui.botao_inicio.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_inicio))
        self.ui.botao_cadastrar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_cadastrar))
        self.ui.botao_listar.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_listar))
        self.ui.botao_cadastrarUsu.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.page_cadUsuario))
        self.ui.botao_cadastrar_2.clicked.connect(lambda: self.cadastrar_usuario())
        self.ui.botao_cadProduto.clicked.connect(lambda: self.cadastrar_produto())
        self.ui.botao_excluir.clicked.connect(lambda: self.excluir_produto())
        self.table_estoque()

    #FUNÇÃO PRA CADASTRAR PRODUTOS NO ESTOQUE
    def cadastrar_produto(self):
        nome = self.ui.txt_nome_P.text()
        quantidade = self.ui.txt_qnt_P.text()
        dataValidade = self.ui.text_data_P.text()
        preco = self.ui.txt_preco_P.text()
        try:
            if (not nome or not quantidade or not dataValidade or not preco):##CHECK SE EXISTEM CAMPOS VAZIOS
                raise (NullValor)##LANÇA A EXCESSÃO CRIADA
            
            else:##SE NÃO TIVER, CADASTRA
                produto = Produto (nome, quantidade, dataValidade, preco)
                produtos.append(produto)
                Produto.cadastrarProduto(nome, quantidade, dataValidade, preco)
                self.msgSucesso("Cadastro realizado com sucesso!")
                self.table_estoque()
                db = DataBase()
                db.conectar()
                db.salvar()
                db.encerrar()

                ##DEIXA OS CAMPOS EM BRANCO
                self.ui.txt_nome_P.setText("")
                self.ui.txt_qnt_P.setText("")
                self.ui.text_data_P.setText("")
                self.ui.txt_preco_P.setText("")

        except NullValor as n:
            NullValor.msgError()

    #FUNÇÃO PARA MOSTRAR UMA MENSAGEM DE SUCESSO
    def msgSucesso (self, texto):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Aviso")
        msg.setText(texto)
        msg.exec_()    

    #FUNÇÃO PARA MOSTRAR UMA MENSAGEM DE ERRO
    def msgErro (self, texto):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Aviso")
        msg.setText(texto)
        msg.exec_()    

    #FUNÇÃO PARA EXCLUIR UM PRODUTO
    def excluir_produto (self):
        id = self.ui.txt_id_excluir.text()   
        if not id:
            self.msgErro("Há campos vazios!")

        
        else:
            db = DataBase()
            db.conectar()
            db.excluirProduto(id)
            db.encerrar()   
            self.table_estoque()
            self.msgSucesso("Excluído com sucesso!")
            

    #FUNÇÃO PARA CADASTRAR USUÁRIOS
    def cadastrar_usuario(self):
        nome = self.ui.txt_nome.text() 
        user = self.ui.txt_usuario.text()
        senha = self.ui.txt_senha.text()
        confirmarsenha = self.ui.txt_confirmarsenha.text()
        try:
            if (not nome or not user or not senha or not confirmarsenha):##CHECK SE EXISTEM CAMPOS VAZIOS
                raise (NullValor)
            else:
                if self.ui.txt_senha.text() != self.ui.txt_confirmarsenha.text():
                    self.msgErro("Senhas divergentes!")
                    return None
                else:        
                    ##CADASTRA USUÁRIO NO BD
                    db = DataBase()
                    db.conectar()
                    db.inserirUsuario(nome, user, senha)
                    db.encerrar()
                    
                    ##MENSAGEM SUCESSO
                    self.msgSucesso("Cadastro realizado com sucesso!")
                    self.ui.txt_nome.setText("")
                    self.ui.txt_usuario.setText("")
                    self.ui.txt_senha.setText("")
                    self.ui.txt_confirmarsenha.setText("")
        
        except NullValor as n:
            NullValor.msgError() 

    #FUNÇÃO PARA ADICIONAR/ATUALIZAR A TABELA DA PAGINA LISTAR
    def table_estoque(self):        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.ui.tableView.setModel(self.model)
        self.model.setTable("Produtos")
        self.model.select()

#VARIÁVEIS GLOBAIS
    
#funcoes

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())