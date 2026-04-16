CREATE DATABASE IF NOT EXISTS codeflavor;
USE codeflavor;

CREATE TABLE IF NOT EXISTS produtos (
codigo INT NOT NULL PRIMARY KEY auto_increment,
destaque BOOL,
produto VARCHAR (200),
descr VARCHAR (500),
preco FLOAT,
foto VARCHAR (500)
);

INSERT INTO  produtos(produto, descr, preco, foto) 
VALUES ("hamburbur", "hamham",345,"https://assets.biggreenegg.eu/app/uploads/2019/03/28145521/topimage-classic-hamburger-2019m04-800x534.jpg")

CREATE TABLE IF NOT EXISTS usuarios (
codigo_usuario INT NOT NULL PRIMARY KEY auto_increment,
nome_perfil VARCHAR (200),
senha VARCHAR (200)
);