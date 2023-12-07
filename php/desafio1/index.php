<style>

.card{
    display: flex;
    flex-wrap: wrap;
    font-family: Arial, Helvetica, sans-serif;
    margin: auto;
    max-width: 1200px;
    overflow: hidden; /* qualquer conteúdo que exceda as dimensões desse elemento será ocultado*/
}

h3, .produto-valor{

    font-family: "Times New Roman", Times, serif;
    font-size: 1.6em; /* o tamanho da fonte será 1.6x o tamanho da fonte do elemento pai*/
    color: #155f67; /*azul esverdedado escuro*/
}

.produto-valor{
    font-weight: bold;
}


.card-item{

    border: 1px solid #ccc;
    margin-left: 10px;
    padding: 5px;
    border-radius: 2px;
    text-align: center;
    width: 350px;
    margin-top: 20px;
    overflow: hidden;

}


.card-item:hover{ /* "hover é uma subclasse na qual permite a estilização de um elemento quando o cursor do mouse passa sobre ele*/
    background-color: #f1f1f1;
    cursor: pointer; /* deixa a mão do cursor do mouse no formato de clique*/
}


.btn-comprar{

    background-color: #155f67;
    padding: 10px 20px;
    margin-bottom: 30px;
    border-radius: 5px;
    color: #fff;
    text-decoration: None;
}


.btn-comprar:hover{/* quando o cursor do mouse passar pelo elemento (botão), ele ficará vermelho*/

    background-color: red;

}

h1{
    text-align: center;
}

</style>


<?php

    $produtos = [
        ['id'=> '1', 'nome'=> 'Notebook', 'valor'=> '1500', 'descrição'=> 'descrição do produto deve aparecer aqui'],
        ['id'=> '2', 'nome'=> 'Guitarra', 'valor'=> '600', 'descrição'=> 'guitarra pesada, mas boa'],
        ['id'=> '3', 'nome'=> 'Monitor LCD', 'valor'=> '850', 'descrição'=> 'monitor com tela LCD, confiável'],
        ['id'=> '4', 'nome'=> 'Mouse Gamer', 'valor'=> 120, 'descrição'=> 'mouse com LED'],
    ];


    echo"<h1>LISTA DE PRODUTOS</h1>";

    foreach ($produtos as $key=> $value){

        

        echo"<div class=\"card\">";

        echo "<div class=\"card-item\">";

        echo "<h3>{$value["nome"]}</h3>";

        echo "<p class=\"produto-descricao\">{$value["descrição"]}</p>";

        echo "<p class=\"produto-valor\"><span>R$</span>{$value["valor"]}</p>";
        echo "<a href=\"\" class=\"btn-comprar\">Comprar</a>";

        echo "</div>";
    }
    

?>




<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DESAFIO 1</title>
</head>
<body>

   <!-- <h1>LISTA DE PRODUTOS</h1>

    <div class="card">

        <div class="card-item">

            <h3>Produto</h3>

            <p class="produto-descricao">Aqui vai a descrição do produto que vai ficar dentro do card</p>

            <p class="produto-valor"><span>R$</span>10,99</p>
            <a href="" class="btn-comprar">Comprar</a>
        
        </div>


        <div class="card-item">

            <h3>Produto</h3>

            <p class="produto-descricao">Aqui vai a descrição do produto que vai ficar dentro do card</p>
            <p class="produto-valor"><span>R$</span>10,99</p>
            <a href="" class="btn-comprar">Comprar</a>


        </div>


        <div class="card-item">


            <h3>Produto</h3>

            <p class="produto-descricao">Aqui vai a descrição do produto que vai ficar dentro do card</p>
            <p class="produto-valor"><span>R$</span>10,99</p>
            <a href="" class="btn-comprar">Comprar</a>

        </div>

    </div> -->




    
</body>
</html>