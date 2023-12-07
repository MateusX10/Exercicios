<?PHP


$numero=5;

for ($i=1; $i<=10; $i+= 1){

    echo "<<< TABUADA DO $i >>>"."<br>";

    for ($j=1; $j<=10; $j++){
        $result = $i * $j;

        echo "$i x $j = $result"."<br>";
    }
}