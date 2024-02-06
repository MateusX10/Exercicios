#use cadastro;

create table funcionarios (
id int NOT NULL AUTO_INCREMENT,
nome varchar(255) NOT NULL,
sexo enum("M", "F"),
nascimento date,
peso decimal(5, 2),
altura decimal(3, 2),
nacionalidade varchar(30) DEFAULT 'Brasil',
PRIMARY KEY(id)
)DEFAULT CHARSET="utf8";


#drop table funcionarios;


alter table funcionarios add cargo varchar(30);


insert into funcionarios (id, nome, sexo, nascimento, peso, altura, nacionalidade, cargo) values(DEFAULT, 'José', 'M', '1950-10-20', '90.10', '1.80', DEFAULT, 'RH');




#alter table funcionarios add cargo varchar(30);

#alter table funcionarios drop column cargo;


#alter table funcionarios add sobrenome varchar(255) after nome;


alter table funcionarios add campo varchar(40) FIRST;


alter table funcionarios modify column nome varchar(200);


alter table funcionarios modify column sobrenome varchar(225);


describe funcionarios;


alter table funcionarios add column carga_horaria varchar(100);


alter table funcionarios modify carga_horaria varchar(100) NOT NULL DEFAULT '';


alter table funcionarios change novo_nome nome varchar(255) NOT NULL;

alter table funcionarios modify column carga_horaria varchar(255) NOT NULL DEFAULT 'Carga';

insert into funcionarios (campo, id, nome, sobrenome, sexo, nascimento, peso, altura,nacionalidade, carga_horaria) values('algo', DEFAULT, 'Maria', 'Candida', 'F', '2020-10-30','66.90', '1.77', 'EUA', '100');


insert into funcionarios (campo, id, nome, sobrenome, sexo, nascimento, peso, altura,nacionalidade, carga_horaria) values('algo', DEFAULT, 'Maria', 'Candida', 'F', '2020-10-30','66.90', '1.77', 'EUA', DEFAULT);


select * from funcionarios;


#escribe funcionarios;


alter table escravos_do_capitalismo rename to funcionarios;
