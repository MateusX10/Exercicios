use cadastro;


select * from cursos;

update cursos set ano='2025' where id_curso='7';


update cursos set ano='2015' where ano='2010';


update cursos set ano='1980' where ano=0;


UPDATE cursos SET ano='2015' WHERE ano='1980' LIMIT 1;


select * from cursos;

update cursos set ano='2025' where id_curso='7';


update cursos set ano='2290' where ano='2015';


update cursos set ano='1980' where ano=0;


UPDATE cursos SET ano='2015' WHERE ano='1980' LIMIT 1;



insert into cursos values ('15','Mestre cuca brabo', '100', '320', '2024');


delete from cursos where id_curso='7';


delete from cursos where id_curso='6';

insert into cursos values ('20', 'Cozinha Árabe', 'Aprenda a ser brabo na cozinha', '40', '20','2020'),
						('21', 'CozinhAaaaaaa', 'Aprenda a ser brabo na cozinha', '40', '20','2020'),
                        ('22', 'CozinhaaÁrabe', 'Aprenda a ser brabo na cozinha', '40', '20','2020'),
                        ('23', 'Cozinaa Árabe', 'Aprenda a ser brabo na cozinha', '40', '20','2020'),
						('24', 'Cozinaa Áraae', 'Aprenda a ser brabo na cozinha', '40', '20','2020');       
                        
                        
delete from cursos where ano='2020' LIMIT 5	;

/* O comando truncate apaga todas as linhas de uma tabela*/

TRUNCATE table cursos;
						
select * from cursos;