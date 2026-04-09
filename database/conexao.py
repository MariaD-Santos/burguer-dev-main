import mysql.connector

def criar_conexao():
    conexao = mysql.connector.connect(
                    host="localhost",
                    port = 3306,
                    user = "root",
                    password = "root",
                    database = "codeflavor"
                )
    
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor