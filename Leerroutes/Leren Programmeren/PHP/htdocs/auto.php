<?php
$servername = "localhost";
$username = "root";
$password = "";

try {
  $conn = new PDO("mysql:host=$servername;dbname=autosoort", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
 // echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  exit();
}

$merk = $_POST['merk'];
$bouwjaar = $_POST['bouwjaar'];
$auto = $_POST['auto'];
$kenteken = $_POST['kenteken'];


$stmt = $conn->prepare("INSERT INTO `auto` (`id`, `Auto`, `bouwjaar`, `merk`, `Kenteken`) VALUES (NULL, '$auto', '$bouwjaar', '$merk', '$kenteken')");
$stmt->execute();

$result = $stmt->setFetchMode(PDO::FETCH_ASSOC); //fetch haal dingens op via associative arrys

$clients =$stmt->fetchAll();
// $response = '{"result":"oke"}';
header("location: auto.html");
echo $response;

?>
