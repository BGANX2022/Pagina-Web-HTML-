<?php
 $conectar = mysqli_connect('localhost','root','D1s3t3c0m','bgan');

 if(!$conectar){
     echo "No conectado";
 }

 $nombre = $_POST['nombre'];
 $email = $_POST['email'];

 $sql = "INSERT INTO datos(nombre, email) VALUES ('$nombre', '$email')";

 $ejecutar = mysqli_query($conectar, $sql);

 if(!$ejecutar){
     echo "Hay algun error";
 }else{
     echo "Datos almacenados correctamente";
 }
?>