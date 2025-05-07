<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['CARGA'])) {
        /* Si accede */
        $NOMBRE = $_POST['NOMBRE'];
        $APELLIDO = $_POST['APELLIDO'];
        $EDAD = $_POST['EDAD'];
        $DNI = $_POST['DNI'];
        $TELEFONO = $_POST['TELEFONO'];
        $CORREO = $_POST['CORREO'];
        $GENERO = $_POST['GENERO'];
        $CONTRA = $_POST['CONTRA'];
        if ($EDAD <= 17) {
            header('Location: MenorEdad.php');
        }
    } else {
        header('Location: index.php');
    }
} else {
    header('Location: index.php'); 
}

?>

<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Club Jazzi</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="Css/Style-Carga.css">
    </head>
    <body>
        <header>
            <a href="index.php">
                <h3>Jazzi</h3>
            </a>
        </header>
        <main>
            <section>
                <h2 class="welcome-title">Bienvenido <?php echo $NOMBRE; ?>!</h2>
                <h3 class="data-title">Datos <span>(verifique que esten correctos)</span> </h3>
                <div class="data-box">
                    <p>Nombre: <?php echo $NOMBRE; ?></p>
                    <p>Apellido: <?php echo $APELLIDO; ?></p>
                    <p>Edad: <?php echo $EDAD; ?></p>
                    <p>DNI: <?php echo $DNI; ?></p>
                    <p>Genero: <?php echo $GENERO; ?></p>
                    <p>Telefono: <?php echo $TELEFONO; ?></p>
                    <p>Correo: <?php echo $CORREO; ?></p>
                    <p>Contraseña: <span class="password-data"><?php echo $CONTRA; ?></span></p>
                </div>
                <h3 class="data-title">Estado</h3>
                <div class="data-box">
                    <p>Vip: No</p>
                    <p>Reservas: No</p>
                    <p></p>
                </div>
            </section>
            <aside>
                <a href="CambiarDatos.php"><h3>Cambiar Datos</h3></a>
                <a href="ERROR-404.php"><h3>Cambiar Correo</h3></a>
                <a href="Reserva.php"><h3>Reservar</h3></a>
                <a href="ERROR-404.php"><h3>Estado VIP</h3></a>
                <a href="index.php"><h3>Cerrar Sesion</h3></a>
            </aside>
        </main>
        
</html>