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
        conexao.commit()
        conexao.close()

        return True