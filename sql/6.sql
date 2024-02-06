# criando a tabela cliente

create table if not exists cliente (
id int AUTO_INCREMENT,
nome varchar(255),
email varchar(40),
telefone varchar(30),
primary key(id)
)DEFAULT CHARSET=utf8;

# descrevendo sobre a tabela cliente
#describe cliente;

# adicionando registros
insert into cliente (id, nome, email, telefone) values (default, 'Pedro', 'pedro@yahoo.com', '+55 (41) 9 9xxx-xxxx'),
(default, 'Maria', 'maria@gmail.com', '+55 (41) 9 9xxx-xxxx'), (DEFAULT, 'José', 'jose@gmail.com', '+55 (41) 9 xxxx-xxxx') ;



# adicionando o campo endereço


alter table cliente add column endereco varchar(30) DEFAULT '';


select * from clientes;



alter table cliente rename to clientes;



alter table clientes modify column email varchar(50) NOT NULL;






