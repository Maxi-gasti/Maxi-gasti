<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Registro Jazzi</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="Css/Style-CamDatos.css">
    </head>
    <body>
        <header>
            <a href="index.php">
                <h3>Jazzi</h3>
            </a>
        </header> 
        <main>
            <form  method="POST"  action="Carga.php">
                <h2>
                    Cambiar Datos
                </h2>
                <fieldset>
                    <legend>Datos Basicos</legend>
                    <label>
                        Nombre
                        <input type="text" name="NOMBRE" placeholder="Maximo"  required>
                    </label>
                    <label>
                        Apellido
                        <input type="text" name="APELLIDO" placeholder="Gasti" required>
                    </label>
                    <label>
                        Edad
                        <input type="number" name="EDAD" placeholder="17" required>
                    </label>
                    <label>
                        DNI
                        <input type="number" name="DNI" placeholder="47521..." required>
                    </label>
                    <label>
                        GENERO
                        <br>
                        <select name="GENERO">
                            <option value="HOMBRE">Hombre</option>
                            <option value="MUJER">Mujer</option>
                            <option value="OTRO">Otro</option>
                        </select>
                    </label>
                </fieldset>

                <fieldset>
                    <legend>Usuario</legend>
                    <label>
                        Correo Electronico
                        <input type="email" name="CORREO" placeholder="Prueba123@gmail.com" required>
                    </label>
                    <label>
                        Contraseña
                        <input type="text" name="CONTRA" placeholder="..." required>
                    </label>
                </fieldset>

                <fieldset>
                    <legend>Contacto</legend>
                    <label>
                        Telefono<span>(Opcional)</span>
                        <input type="text" name="TELEFONO" placeholder="343 541..." >
                    </label>
                    
                </fieldset>
                
                <input  type="submit" name="CARGA" value="Enviar" class="input-submit">
            </form>
        </main>
    </body>
</html>