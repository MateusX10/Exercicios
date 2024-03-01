# Importa a biblioteca "sqlite3"
import sqlite3


# cria uma conexão com o banco de dados "people.db"
connection = sqlite3.connect("people.db")


# cria o objeto "cursor" para que você possa executar comandos sql no bano de dados "people.db"
cursor = connection.cursor()


# cria a tabela, caso não exista
cursor.execute("create table if not exists user (id integer primary key, name text, username text, email text, created_at date)")


#cursor.execute("insert into user (id, name, username, email, created_at) values(1, 'Mateus', 'matX10', 'mateus@gmail.com', '2024-02-29');")

#cursor.execute("insert into user (id, name, username, email, created_at) values (2, 'João', 'joao30', 'joao@gmail.com', '2024-03-01');")


# faz o comando de seleção dos registros da tabela "user"
cursor.execute("select * from user;")

# recupera o resultado da última consulta SQL feita e a imprime na tela
print(cursor.fetchall())

# Faz o commit das alterações na tabela do banco de dados
connection.commit()

# Fecha a conexão com o banco de dados
connection.close()

