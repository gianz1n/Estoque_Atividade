create database Estoque;
use Estoque;

create table Fabricante(
cod_fabricante int auto_increment, 
nome_fabricante varchar(70),
primary key (cod_fabricante)
);

create table Produto(
cod_produto int auto_increment,
nome_produto varchar(70),
fabricante_produto varchar(70),
quantidade_produto int  not null,
primary key(cod_produto)
);

create table Historico_compra(
cod_historico int auto_increment,
cod_produto_hc varchar(60) not null,
data_hc date not null,
quantidade_hc int not null,
primary key(cod_historico)
);

create table Historico_venda(
cod_historicov int auto_increment,
cod_produto_hv varchar(60) not null,
data_hv date not null,
quantidade_hv int not null,
primary key(cod_historicov)
);



#select * from Produto;
#select * from Fabricante;
select * from Historico_compra;
drop database Estoque;


