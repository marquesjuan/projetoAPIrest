create database if not exists projetoapi;
use projetoapi;

create table if not exists usuario(
id int auto_increment primary key,
nome varchar(255) not null,
email varchar(255) not null unique,
senha varchar(255) not null
);

create table if not exists produto(
id int auto_increment primary key,
nome varchar(255) not null,
preco decimal(10,2) not null,
quantidade int default 0
);

create table if not exists carrinho(
id int auto_increment primary key,
id_produto int,
quantidade int default 1,
foreign key(id_produto) references produto(id) on delete cascade
);


insert into usuario (nome,email,senha) values
('teste','teste@teste.com','teste');
