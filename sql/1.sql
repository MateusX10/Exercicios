create table funcionarios (
id int AUTO_INCREMENT,
nome varchar(100) NOT NULL,
sexo enum('M', 'F'),
nascimento date,
email varchar(50),
telefone varchar(25),
PRIMARY KEY (id)
)DEFAULT CHARSET=utf8;

/*drop table funcionarios*/

insert into funcionarios (nome, sexo, nascimento, email, telefone) values ("Maria", "F", '1989-12-12', "maria@email.com", "+55 (41) 9xxxx-xxxx");

insert into funcionarios (nome, sexo, nascimento, email, telefone) values ("Roberto", "M", '1999-03-20', "roberto@email.com", "+55 (41) 9xxxx-xxxx");

insert into funcionarios (nome, sexo, nascimento, email, telefone) values ("Vitória", "F", '2000-10-10', "vitoria@email.com", "+55 (40) 9xxxx-xxxx");

insert into funcionarios (nome, sexo, nascimento, email, telefone) values ("Brian", "M", '1995-06-10', "brian@email.com",  "+55 40 9xxxx-xxxx");

insert into funcionarios (nome, sexo, nascimento, email, telefone) values ("Zec", "M", '2006-12-12', "zec@email.com", '+55 (35) 9xxxx-xxx');


select * from funcionarios;

set @ano_atual = YEAR(NOW());

select * from funcionarios where (@ano_atual - YEAR(nascimento)) > 25 and id % 2 = 0;

select * from funcionarios;


delete from funcionarios where id = 5;


select * from funcionarios;

update funcionarios set nascimento='1995-06-15' where id=4;


select nome, nascimento from funcionarios;
select "Estamos no ano ", @ano_atual;

create table departamento (
id_departamento int AUTO_INCREMENT,
id_funcionario int,
FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id),
PRIMARY KEY (id_departamento)
)DEFAULT CHARSET=UTF8;


select * from departamento;

/*delete from funcionarios;*/

select * from funcionarios;