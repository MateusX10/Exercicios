<?php


$n1 = 5;

$n2 = 10;

$mensagem = "hello;world";

$resultado = ($n1 > $n2) ? "n1 é maior do que n2" : "n1 é menor do que n2";

$resultado_mensagem = ($mensagem == "hello; world") ? "hello; world": "something went wrong...";




echo "O valor da variável resultado é $resultado";

echo "<br>O valor da variável 'resultado da mensagem' vale $resultado_mensagem";



$v1 = 10;

$v2 = "10";


$result = ($v1 == $v2) ? "são iguais" : "não, é diferente"; //comparação normal com  conversão de tipos


echo "<br>$result"."<br>";


$result = ($v1 === $v2) ? "são iguais" : "são diferentes"; //comparação estrita (sem conversão entre tipos)

echo "$result"."<br>";




$cont = 0;

$total = 15;


while ($cont <= $total){
    echo "contador = ".$cont."<br>";
    $cont += 1;
}