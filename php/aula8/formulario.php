<form  method="get" action="http://localhost/CURSO_PHP/css/aula8/index.php">

    <?php


        $pag = ( isset($_GET['pag']) ) ? $_GET['pag'] : '';

        $nome = ( isset($_GET['nome']) ) ? $_GET['nome'] : '';

        $idade = ( isset($_GET['idade'])) ? $_GET['idade'] : '';


        if ($nome == ''){
    
    ?>

    <label for="nome">Nome: </label>
    <input type="text" placeholder="digite seu nome" name="nome" required>
    <label for="idade">Idade: </label>
    <input type="text" placeholder="digite sua idade" name="idade" required>
    <input type="text" name="pag" value="formulario" hidden>
    <input type="submit" required>


    <?php

        } else{
            echo "olá $nome, você tem $idade anos";
        }

    ?>
</form>