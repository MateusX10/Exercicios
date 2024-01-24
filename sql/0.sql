use cadastro;

#create database cadastro 
#DEFAULT character set utf8
#DEFAULT COLLATE utf8_general_ci;

#use cadastro;


create table pessoas (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(30) NOT NULL,
    nascimento date,
    sexo enum("M","F"),
    peso decimal(5,2),
    altura decimal(3,2),
    nacionalidade varchar(20) DEFAULT 'Brasil',
    PRIMARY KEY (id)
)DEFAULT CHARSET=utf8;


insert into pessoas values(DEFAULT, 'José', '1955-12-12', 'M', '100.10', '1.90', 'Portugal'),
(DEFAULT, 'Maria', '1959-01-24', 'F', '70.00', '1.65', 'EUA'),
(DEFAULT, 'Reginaldo', '1980-04-01', 'M', '88.10', '1.79', DEFAULT);

describe pessoas;

select * from pessoas;