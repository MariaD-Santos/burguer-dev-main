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