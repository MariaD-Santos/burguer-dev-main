CREATE DATABASE IF NOT EXISTS codeflavor;
USE codeflavor;

CREATE TABLE IF NOT EXISTS produtos (
codigo INT NOT NULL PRIMARY KEY auto_increment,
destaque BOOL default 1,
produto VARCHAR (200),
descr VARCHAR (500),
preco FLOAT,
foto VARCHAR (500)
);

INSERT INTO  produtos(produto, descr, preco, foto) 
VALUES ("hamburbur", "hamham",345,"https://assets.biggreenegg.eu/app/uploads/2019/03/28145521/topimage-classic-hamburger-2019m04-800x534.jpg");

CREATE TABLE IF NOT EXISTS usuarios (
codigo_usuario INT NOT NULL PRIMARY KEY auto_increment,
nome_perfil VARCHAR (200) unique,
senha VARCHAR (200)
);


CREATE TABLE IF NOT EXISTS carrinhos (
	cod_carrinho INT PRIMARY KEY auto_increment,
    usuario int,
    data datetime default current_timestamp,
    finalizado bool,
    CONSTRAINT fk_cod_usuario
    FOREIGN KEY (usuario) REFERENCES usuarios(codigo_usuario)
);

CREATE TABLE IF NOT EXISTS itens_carrinho (
	cod_item_carr INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    CONSTRAINT fk_prodcarrinho_carr
    FOREIGN KEY (cod_carrinho) REFERENCES carrinhos(cod_carrinho),
    CONSTRAINT fk_itenscarrinho_produto 
    FOREIGN KEY (cod_produto) REFERENCES produtos(codigo)
);


select carrinhos.cod_carrinho, usuarios.nome_perfil, carrinhos.data, carrinhos.finalizado, produtos.produto, itens_carrinho.quantidade, produtos.preco, produtos.foto from carrinhos
INNER JOIN itens_carrinho ON carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
INNER JOIN produtos ON produtos.codigo = produtos.codigo;