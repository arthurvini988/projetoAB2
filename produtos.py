#import
from database import *

#class
class Produto:
    def __init__ (self, nome, quantidade, dataValidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.dataValidade = dataValidade
        self.preco = preco
    
    def cadastrarProduto (nome, quantidade, dataValidade, preco):
        db = DataBase()
        ##produto = Produto (nome, quantidade, dataValidade, preco)
        db.conectar()
        db.inserirProduto (nome, quantidade, dataValidade, preco)
        db.encerrar()
        return True
     
    def getNome (self):
        return self.nome
    
    def getQuantidade (self):
        return self.quantidade
    
    def getDataValidade (self):
        return self.dataValidade
    
    def getPreco (self):
        return self.preco
    
    def setNome (self, nome):
        self.nome = nome

    def setQuantidade (self, qnt):
        self.quantidade = qnt

    def setDataValidade (self, data):
        self.dataValidade = data
    
    def setPreco (self, preco):
        self.preco = preco

    def __repr__(self):
        return str(self.__dict__)


