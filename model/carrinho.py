from database.conexao import criar_conexao


def cadastro_usuario(nome_perfil:str) -> list:

        conexao, cursor =  criar_conexao()

        cursor.execute(""" 
                    select  from 
                            """)
        conexao.commit()
        conexao.close()

        return True