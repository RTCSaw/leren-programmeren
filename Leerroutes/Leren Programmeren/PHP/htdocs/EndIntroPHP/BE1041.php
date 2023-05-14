<?php
$huidigUur = date('H');
$hallo = '';
$achtergrond = '';

if($huidigUur >= 6 && <= 12){
    $achtergrond = 'moring.png';
    $hallo = 'Goede morgen';
}
elseif($huidigUur>=12 && <=18){
    $achtergrond = 'afternoon.png';
    $hallo = 'Goede middag';
}
elseif($huidigUur >=18 && <=00){
    $achtergrond = 'evening.png';
    $hallo = 'Goede avond';
}
else{
    $achtergrond= 'night.png';
    $hallo = 'Goede Nacht'
}