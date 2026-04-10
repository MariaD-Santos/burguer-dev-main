from database.conexao import criar_conexao

def rec_produtos():
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    SELECT produto, descr, destaque ,preco, foto from produtos;
                    """)
    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def rec_destaq():
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    SELECT destaque, foto from produtos where destaque = 1;
                    """)
    destaques = cursor.fetchall()
    conexao.close()
    return destaques

def recuperar_produto(codigo:int):
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    SELECT produto, descr, destaque ,preco, foto from produtos WHERE codigo= %s;
                    """, [codigo])
    produto = cursor.fetchone()
    conexao.close()
    return produto