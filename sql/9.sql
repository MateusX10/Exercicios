use cadastro;


create table IF NOT EXISTS internauta (
id int AUTO_INCREMENT,
username varchar(255) NOT NULL,
nascimento date,
genero enum('M', 'F'),
email varchar(255),
PRIMARY KEY (id)
)DEFAULT CHARSET=utf8;


insert into internauta values(DEFAULT, 'user261', '2001-02-19', 'M', 'user261@gmail.com');


select * from internauta;


update internauta set username='user260', email='user261@gmail.com' where id=1;

insert into internauta values(DEFAULT, 'maria', '2010-04-09', 'F', 'maria@gmail.com'),
							 (DEFAULT, 'joao', '1995-01-20', 'M', 'joao@gmail.com'),
                             (DEFAULT, 'bananinha330', '2011-12-19', 'M', 'bananinha2@gmail.com');
                             
                             
delete from internauta where id=4;

alter table internauta add column nacionalidade varchar(100) DEFAULT '';


TRUNCATE internauta;


select * from internauta;