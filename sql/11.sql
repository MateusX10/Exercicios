create database Dispositivos;

use Dispositivos;

create table if not exists Computadores(
id int AUTO_INCREMENT,
marca varchar(255) NOT NULL,
cor varchar(100),
PRIMARY KEY(id)
)DEFAULT CHARSET=utf8;


describe Computadores;

insert into Computadores(marca, cor) values("DELL", "preto"),
									 ("POSITIVO", "azul"),
                                     ("APPLE", "PRETO");
                                     
select * from Computadores;


update Computadores set marca="ACER" where id = 3;

update computadores set marca="apple" where id=2;


insert into Computadores values(DEFAULT, "HP", "VERDE");


select * from Computadores;


delete from Computadores where id=4;


select * from Computadores;


alter table Computadores add column ram varchar(255) NOT NULL DEFAULT '8';

alter table Computadores drop column ram;


alter table Computadores add column ram varchar(255) DEFAULT '8';

alter table Computadores drop column ram;


select * from Computadores;


alter table Computadores add column ram varchar(255) NOT NULL;


select * from Computadores;


alter table Computadores drop column ram;


alter table Computadores add column ram varchar(255) NOT NULL DEFAULT '8';

select * from computadores;


TRUNCATE table Computadores;


drop database Dispositivos;