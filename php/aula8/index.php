<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TABUADA(?)</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <div class="header"><a href="./index.php"><button>home</button></a></div>
    </header>
    <section class="corpo">
        <div class="sidebar">
            <a href="http://localhost/CURSO_PHP/css/aula8/index.php?pag=tabuada">
            <button>Exibir a tabuada</button></a>
            <a href="http://localhost/CURSO_PHP/css/aula8/index.php?pag=formulario"><button>Formulário</button></a>
        </div>
        <div class="content">

            <?PHP

                $paginaParaExibir = ( isset($_GET['pag'])) ? $_GET['pag']: '';

                switch ($paginaParaExibir){

                    case "tabuada":

                        include "tabuada.php";
                        break;

                    case "formulario":

                        include "formulario.php";

                        break;

                    case '':

                        echo include "inicial.php";

            }

            
            ?>

        </div>
    </section>
    
    <footer>
        Footer
    </footer>
    

</body>
</html>