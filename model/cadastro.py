from database.conexao import criar_conexao

def cadastro_usuario(nome_perfil:str, senha:str):
    try:
        conexao, cursor =  criar_conexao()

        cursor.execute(""" INSERT INTO usuarios(nome_perfil, senha) 
                            VALUES(%s,%s)""",
                            [nome_perfil, senha])
        
        conexao.commit()
        conexao.close()

        return True
        
    except Exception as e:
        print (e)
        return False

class Usuario:
    def __init__(self, usuario:str, senha:str):
        self.usuario = usuario
        self.senha = senha

    def cadastrar(self):
        
            conexao, cursor = conexao()

            cursor.execute("""

                        INSERT INTO cadastro
                        (usuario, senha)
                        VALUES
                        (%s, %s)
                           """, [self.usuario, self.senha])
            conexao.commit()
            conexao.close()

            return True
    

    def logar(usuario:str, senha:str) ->dict:
         conexao, cursor = conexao()
         cursor.execute("""
            SELECT * FROM cadastro WHERE usuario = %s and senha = %s
                        """, [usuario, senha])
         resultado = cursor.fetchone()
         conexao.close()
         return resultado