<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    
    function som_even_getallen($getallen) {
        $som = 0;
    
        foreach ($getallen as $getal) {
            if ($getal % 2 === 0) {
                $som += $getal;
            }
        }
    
        return $som;
    }
    
    $getallenLijst = [1, 2, 3, 4,10,14];
    $resultaat = som_even_getallen($getallenLijst);
    echo $resultaat; // Output: 6


        
    // OPDRACHT 2
    function lengtewoord($words) {
        $words = explode(' ', $words);
        $longestWordLength = 0;
        $longestWord = '';
    
        foreach ($words as $word) {
            if (strlen($word) > $longestWordLength) {
                $longestWordLength = strlen($word);
                $longestWord = $word;
            }
        }
    
        return $longestWord; // Geef het langste woord terug
    }
    
    $words = "Where did the big Elephant go?";
    $longestWord = lengtewoord($words);
    echo $longestWord;

    // OPDRACHT 3
    function sort_lijst_asc($array) {
        $to_sort = true;
        while ($to_sort) {
            $to_sort = false;
            for ($x = 0; $x < count($array) - 1; $x++) {
                if ($array[$x] > $array[$x + 1]) {
                    list($array[$x], $array[$x + 1]) = array($array[$x + 1], $array[$x]);
                    $to_sort = true;
                }
            }
        }
        return $array;
    }
    
    print_r(sort_lijst_asc([5, 3, 2]));
    print_r(sort_lijst_asc([67, 15, 22, 68, 3]));
    

    ?>
    
</body>
</html>