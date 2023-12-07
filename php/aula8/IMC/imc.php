<?php

$nome = ( isset($_POST['nome'])) ? $_POST['nome'] : '';

$peso = ( isset($_POST['peso'])) ? $_POST['peso'] : '';

$altura = ( isset($_POST['altura'])) ? $_POST['altura'] : '';

if ( $nome != ''){

    $imc = $peso / ($altura ** 2);

    $imc = number_format($imc, 2, '.', '');
    echo "$nome, seu imc é $imc";
}

else{

?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <form method="post" action="http://localhost/CURSO_PHP/css/aula8/IMC/index.php">
        <label for="nome">Nome:</label><br>

            <input type="text" placeholder="digite seu nome" name="nome" id="nome" required><br>

        <label for="peso">Peso:</label><br>

            <input type="number" placeholder="digite seu peso" name="peso" id="peso" step="0.01" required><br>

        <label for="altura">Altura</label><br>

            <input type="number" placeholder="digite sua altura" name="altura" id="altura" step="0.01" required><br>

        <input type="text" value="imc" name="pag" hidden><br>

        <input type="submit" value="calcular">
    </form>
    
</body>
</html>


<?php

}