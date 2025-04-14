<form method="POST" action="Procesar.php">
	Ingrese su nombre
	<input type="text" name="NOMBRE" required><br><br>
	Ingrese su edad
	<input type="number" name="EDAD" required><br><br>
	Ingrese su mascota
	<select name="MASCOTA">
		<option value="Perro">Perro</option>
		<option value="Gato">Gato</option>
		<option value="Loro">Loro</option>
		<option value="Pez">Pez</option>
	</select><br><br>
	Ingrese su color
	<input type="color" name="COLOR" required><br><br>
	<input type="submit" value="Enviar" name="CARGAR">
</form>