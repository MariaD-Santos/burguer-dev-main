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