<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eindopdracht van de intro</title>
    <link rel="stylesheet" href="BE104.css">
</head>
<body>
    <div id="Hallo">
        <?php
            $huidigUur = date('H');
            $hallo = '';
            $achtergrond = '';

            if($huidigUur >= 6 && 12){
                $hallo = 'Goede morgen';
                $achtergrond = 'moring.png';
                
            }
            elseif($huidigUur>=12 && 18){
                $hallo = 'Goede middag';
                $achtergrond = 'afternoon.png';
                
            }
            elseif($huidigUur >=18 && 00){
                $hallo = 'Goede avond';
                $achtergrond = 'evening.png';
            }
            else{
                $hallo = 'Goede Nacht';
                $achtergrond= 'night.png';
            }
            echo '<h1>'.$hallo . '<h1>';
            echo '<p> Het is nu ' . date('H:i') . '</p>';
            ?>
    </div>
</body>
</html>