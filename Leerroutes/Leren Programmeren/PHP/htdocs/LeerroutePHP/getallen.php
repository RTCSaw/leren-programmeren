<?php
$getal1 = (rand(10,100));
$getal2 = (rand(10,100));

$uitkomst1 = $getal1 - $getal2;
echo " $getal1 - $getal2= $uitkomst1<br>";

$uitkomst2 = $getal1 * $getal2;
echo " $getal1 * $getal2 = $uitkomst2<br>";

$uitkomst3 = $getal1 + $getal2;
echo " $getal1 + $getal2 = $uitkomst3<br>";

$uitkomst4 = $getal1 / $getal2;
echo " $getal1 / $getal2 = $uitkomst4<br>";

$tafel = 6;
for ($x = 1; $x <= 10; $x++) {
    $uitkomst = $x * $tafel;
    echo $x . " x " . $tafel . " = " . $uitkomst . "<br>";
}

function vermenigvuldig($tafel) {
    for ($x = 1; $x <= 10; $x++) {
        $uitkomst = $x * $tafel;
        echo $x . " x " . $tafel . " = " . $uitkomst . "<br>";
    }
}

vermenigvuldig(6);
?>
