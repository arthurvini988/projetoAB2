import sqlite3
import pickle

class DataBase():
    def __init__(self, name = "system.db"):
        self.name = name

    def conectar (self):
        self.connection = sqlite3.connect(self.name)

    def encerrar (self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users (self):
        try:
            comando = self.connection.cursor()
            comando.execute("""
            
                CREATE TABLE IF NOT EXISTS users (
                
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                );
            
            """
            )
        except AttributeError:
            print ("Faça a conexão!")

    def create_table_produtos (self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                CREATE TABLE IF NOT EXISTS produtos (
                
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    dataValidade DATE NOT NULL,
                    preco FLOAT NOT NULL
                );
            
            """
            )
        except AttributeError:
            print ("Faça a conexão!")
     
    def excluirProduto (self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                DELETE FROM produtos WHERE id = ?

            """, (id,))
            self.connection.commit()
            
        except AttributeError:
            print ("Faça a conexão!")        
            
    def inserirUsuario (self, nome, usuario, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO users(nome, user, password) VALUES(?,?,?); 
            
            
            """,(nome, usuario, senha,))
            self.connection.commit()

        except AttributeError:
            print ("Faça a conexão!")

    def inserirProduto (self, nome, quantidade, dataValidade, preco):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO produtos(nome, quantidade, dataValidade, preco) VALUES(?,?,?,?); 
            
            
            """,(nome, quantidade, dataValidade, preco))
            self.connection.commit()

        except AttributeError:
            print ("Faça a conexão!")
        
    def check_user (self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT * FROM users;
            
            """)

            for linha in cursor.fetchall():
                if (linha[2].upper() == user.upper() and linha[3] == password):
                    return True
                
                else:
                    continue
            return "Sem acesso."

        except:
            pass
        
    def salvar (self):
        cursor = self.connection.cursor()
        cursor.execute("""
            
            SELECT * FROM produtos;

            """)
            
        for linha in cursor.fetchall():
            produtos.append (linha)
        with open ("dados.dat", "wb") as arquivo:
            pickle.dump(produtos, arquivo)

global produtos
produtos = []

if __name__ == "__main__":
    db = DataBase()
    db.conectar()
    db.create_table_produtos()
    db.create_table_users()
    db.encerrar()