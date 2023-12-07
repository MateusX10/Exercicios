<?php

function quebraLinha(){
    echo "<br>";
}

/*$frutas = array("banana", "Morango", "abacate");

print_r($frutas);

quebraLinha();

 Array associativo
$carro = array('cor'=> 'azul', 'velocidade máxima'=> '100 km/h');

print_r($carro);

quebraLinha();

// array multidimensional
$carros = array('esportivos'=> array('Porche', 'Ferrari'),
                'passeio'=> array('corolla', 'civic'));


print_r($carros);


quebraLinha();


echo "{$carros['passeio'][0]}";

quebraLinha();


# as chaves "{}" convertem em string, logo você pode as utilizar para imprimir arrays #com o echo
*/

//echo  "{$carros['esportivos'][1]}";

/*
$frutas1 = array("banana", "mamão", "maçã");

$frutas2 = array("pêssego", "pera", "kiwi", "laranja");

# adiciona um elemento no início da array
array_unshift($frutas1, "melancia");

array_push($frutas1, "morango");

$todas_as_frutas = array_merge($frutas1, $frutas2);

# remove o primeiro elemento da array
array_shift($todas_as_frutas);

# remove o último elemento da array
array_pop($todas_as_frutas);

echo "Frutas 1: ";
print_r($frutas1);

quebraLinha();

echo "Frutas 2: ";

print_r($frutas2);

quebraLinha();

echo "Todas as frutas: ";

print_r($todas_as_frutas);
*/

# retornar as chaves (índices da array)

/*$teste = array("cor"=> "azul", "tamanho"=> "199cm");

print_r(array_keys($teste));


quebraLinha();

# retorna os valores da array

print_r(array_values($teste));


quebraLinha();

# contar o númer de elementos de uma array
print_r(count($teste));
*/


/*$jogos = array("clash royale", "minecraft", "undertale", "celest");

if (in_array("celest", $jogos)){
    echo "de fato, o elemento está na array";
}else{
    echo "não, o elemento não está na array";
}*/

/*
$cesta_de_frutas = array("morango", "banana", "maçã");

foreach($cesta_de_frutas as $key=>$value){
    echo "$key: $value <br>";
}*/


$produtos = [
    ['id'=> 1, 'nome'=> 'produto 1', 'valor'=> "200.50"],
    ['id'=> 2, 'nome'=> 'produto 2', 'valor'=> "45.0"],
    ['id'=> 3, 'nome'=> 'produto 3', 'valor'=> '20.85'],   
];

$produtos_acima_de_cinquenta_reais = array_filter($produtos, function($produto){

    return $produto['valor'] > 150;

})                                                                                                                      
;

print_r($produtos_acima_de_cinquenta_reais);