<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMC</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <a href="http://localhost/CURSO_PHP/css/aula8/IMC/index.php"><button>Home</button></a>
    </header>

    <section>

        <div class="sidebar">
            
            <a href="http://localhost/CURSO_PHP/css/aula8/IMC/index.php?pag=imc"><button>IMC</button></a>

            
    
        </div>

       

       <div class="content">

        <?php
            $conteudoExibido = ( isset($_POST["pag"])) ? $_POST["pag"] :"";



            switch ($conteudoExibido){
                
                case "imc":

                    include "imc.php";
                    break;

                case "":
                    include "inicial.php";
                    break;
            }

            ?>

       </div>

    </section>

    <footer>
        Footer
    </footer>

    
</body>
</html>