<?php


# abrindo uma conexão ao banco de dados
$db = new PDO('sqlite:database.db');

# obtém data atual
$data = date('Y-m-d');

$rows = $db->exec("insert into users (name, email, created_at) values('Roberto', 'roberto@email.com', $data);");

echo "Foram inseridas um total de tantas linhas no banco $rows";

echo PHP_EOL;

$stmt = $db->prepare('select * from users;');

$stmt->execute();

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);
