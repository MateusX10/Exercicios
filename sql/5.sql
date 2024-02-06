#use cadastro;

create table if not exists cursos (
nome varchar(30) NOT NULL UNIQUE,
descricao text,
carga int UNSIGNED, /*sem sinal --> não permite valores negativos*/
totalaulas int,
ano year DEFAULT '2022'
)DEFAULT CHARSET=utf8;

drop table cursos;


alter table cursos add column prof varchar(255) NOT NULL AFTER DESCRICAO;


alter table cursos add column id_curso int FIRST;

alter table cursos add PRIMARY KEY(id_curso);

describe cursos;






create table teste (
id int auto_increment,
nome varchar(30) NOT NULL unique,
idade int,
primary key (id)
);



insert into teste values(DEFAULT, 'Cachorro', '13');


select * from teste;


drop table if exists teste;