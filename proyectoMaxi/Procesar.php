<?php
    if (isset($_POST["CARGAR"])){
    $NOMBRE = $_POST ["NOMBRE"];
    $EDAD = $_POST ["EDAD"];
    $MASCOTA = $_POST ["MASCOTA"];
    $COLOR = $_POST ["COLOR"];
	echo 'Nombre: '.$NOMBRE ."<br>";
	echo 'Edad: '.$EDAD."<br>";
	echo 'Mascota: '.$MASCOTA."<br>";
	echo 'Color: '.$COLOR."<br>";
    }
    else {
       echo "No te pases gil te voy a hackear mogolico de mieradasidjasojdasojoasj";

    }
?>