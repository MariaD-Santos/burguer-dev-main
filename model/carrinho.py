from database.conexao import criar_conexao


def recuperar_carrinho(nome_perfil:str) -> list:

        conexao, cursor =  criar_conexao()

        cursor.execute(""" 
                    select carrinhos.cod_carrinho, usuarios.nome_perfil, carrinhos.data, carrinhos.finalizado, produtos.produto, itens_carrinho.quantidade, produtos.preco, produtos.foto from carrinhos
                        INNER JOIN itens_carrinho ON carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
                        INNER JOIN produtos ON produtos.codigo = produtos.codigo
                        INNER JOIN usuarios ON usuarios.nome_perfil = usuarios.nome_perfil;
                        WHERE carrinhos.usuario = %s
                            """, [nome_perfil])
      

        carrinho = cursor.fetchall()

        conexao.commit()
        conexao.close()

        return carrinho

def inserir_item(nome_perfil, cod_produto, quantidade):
    conexao, cursor = criar_conexao()
    cursor.execute("""
                select cod_carrinho from carrinhos
                where usuario = %s
                and finalizado = 0
                limit 1;

    """, [nome_perfil])


    resultado_carrinho = cursor.fetchone()
    

    if resultado_carrinho:
        cod_carrinho = resultado_carrinho["cod_carrinho"]

    else:
        cursor.execute("""

                INSERT INTO carrinhos(nome_perfil, finalizado)
                VALUES (%s, 0);
    """, [nome_perfil],)
        
    cod_carrinho = cursor.lastrowid


    cursor.execute("""

            INSERT INTO itens_carrinho(cod_carrinho, cod_produto, quantidade)
                   VALUES(%s, %s, %s)
    """, [cod_carrinho, cod_produto, quantidade])
    
    conexao.commit()
    conexao.close()