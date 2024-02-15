#use cadastro;

#select * from funcionarios;

#alter table funcionarios drop column campo;


#alter table funcionarios modify carga_horaria int NOT NULL DEFAULT '5';


#update funcionarios set carga_horaria='10' where id % 2 != 0;

select * from funcionarios;

insert into funcionarios (id, nome, sobrenome, sexo, nascimento, peso, altura, nacionalidade, carga_horaria) values ('4', 'Roberto', 'Guimarães', 'M', '2000-10-10', '66.4', '1.80', 'Brasil', '30');

delete from funcionarios where id='4';



select * from funcionarios;



select * from funcionarios where carga_horaria <=30;


alter table funcionarios rename to funcs;


select * from funcs;


truncate table funcs;


select * from funcs;



alter table funcs rename to funcionarios;


select * from funcionarios;






