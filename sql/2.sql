#create database animes;
use animes;

create table genero_acao (
id INT AUTO_INCREMENT,
nome varchar(255),
ano_lancamento date DEFAULT '2023-10-22',
quantidade_personagens BigInt,
PRIMARY KEY (id)
)DEFAULT CHARSET= utf8;

#describe genero_acao;


#select * from genero_acao;


insert into genero_acao (nome, ano_lancamento, quantidade_personagens) values ("One Piece", '1999-10-15', 1000);
insert into genero_acao (nome, ano_lancamento, quantidade_personagens) values ("Naruto", '2002-03-10', 450);
insert into genero_acao (nome, ano_lancamento, quantidade_personagens) values ("MHA", '2004-04-05', 70);
insert into genero_acao (nome, ano_lancamento, quantidade_personagens) values ("DBZ", '1985-10-10', 500);

#alter table genero_acao AUTO_INCREMENT=3;

#select * from genero_acao;

select * from genero_acao where quantidade_personagens > 100 and id % 2 = 0;


#set @one_piece_ano_de_lancamento =  select year(ano_lancamento) from genero_acao where id=1;



update genero_acao set quantidade_personagens=1087 where id=1;


set @ano_atual = YEAR(NOW());



select @ano_lancamento_one_piece := YEAR(ano_lancamento) from genero_acao where id=1;

select @ano_lancamento_one_piece as ano_lancamento_op;


set @quantidade_de_anos_em_exibicao_one_piece = @ano_atual - @ano_lancamento_one_piece;

select @quantidade_de_anos_em_exibicao_one_piece;


show databases;


select "One Piece estreiou em 1999, logo está em exibição há ", @quantidade_de_anos_em_exibicao_one_piece, "anos";