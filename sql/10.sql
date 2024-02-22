use cadastro;

select * from cursos;

describe funcionarios;

desc pessoas;


select * from funcionarios;

select * from pessoas;


/* excluindo todos os bancos de dados  para assim testar o backup de segurança*/



select * from pessoas;


truncate table pessoas;


drop database test;


drop database minhaloja;


drop database animes;


drop database cadastro;

 # banco "cadastro" não mais existe
use cadastro;


#  Após importar o banco "cadastro" do arquivo de dumb


use cadastro;


select * from animais;


show tables;

describe funcionarios;

describe cursos;

describe pessoas;


describe usuarios;


select * from pessoas;


select * from cursos;

select * from funcionarios;


select * from internauta;


select * from usuarios;