from database.conexao import criar_conexao

def rec_produtos():
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    SELECT produto, descr, preco, foto from produtos;
                    """)
    produtos = cursor.fetchall()
    conexao.close()
    return produtos