<?php 
    var_dump($_REQUEST); echo "<br>";
    var_dump($_GET); echo "<br>";
    var_dump($_POST); echo "<br>";
    echo $_POST['argument']; echo "<br>";

    if(isset($_POST["argument"])){
        echo $_POST["argument"];
    } else {
        echo "remark bestaat niet";
    }

?>