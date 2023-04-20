<?php
$servername = "localhost";
$username = "root";
$password = "";

try {
  $conn = new PDO("mysql:host=$servername;dbname=auto", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
 // echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  exit();
}
$stmt = $conn->prepare("INSERT INTO `auto` (`id`, `Auto`, `bouwjaar`, `merk`, `Kenteken`) VALUES (NULL, 'automaat', '2021', 'Mazda', '123CA21');");
$stmt->execute();

$response = '{"result":"oke"}';
header("Content-type:application/json");
echo $response;

?>
