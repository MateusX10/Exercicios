<?php

$nome = "José";

$idade = 90;

$idade2 = "5";

$idadePorExtenso = "noventa e cinco";

$idadeFinal = ($idade + $idade2);

$ano_nascimento = date("Y") - $idade;

echo "$nome, você nasceu no ano $ano_nascimento";


echo "<br>Sua idade é $idadeFinal (".$idadePorExtenso.")";