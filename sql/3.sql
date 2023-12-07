insert into funcionarios (nome, nascimento, cargo, salario) values ("Joana", '1998-06-22', 'Programador Pleno', 6200.90);
insert into funcionarios (nome, nascimento, cargo, salario) values ("Maria", '1987-10-08', 'Programador Sênior', 7990.90);

insert into funcionarios (nome, nascimento, cargo, salario) values ("Ana", '1999-09-20', "RH", 3200.20);

update funcionarios set cargo="Gerente", salario=7000 where id=1;

SET SQL_SAFE_UPDATES=0;

delete from funcionarios where nome='Ana' and cargo='RH';

select * from funcionarios;


TRUNCATE funcionarios;