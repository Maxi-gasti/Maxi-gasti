<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Reservar</title>
        <link rel="stylesheet" href="Css/Style-Reserva.css">
    </head>
    <body>
         <header>
            <a href="index.php">
                <h3>Jazzi</h3>
            </a>
        </header>
        <main>
            <form method="POST" action="ERROR-404.php">
                <h3>RESERVAR</h3>
                <fieldset>
                    <legend>Lugar\Fecha</legend>
                    <label>Horario
                        <select>
                            <option>7:00pm</option>
                            <option>7:30pm</option>
                            <option>8:00pm</option>
                            <option>8:30pm</option>
                            <option>9:00pm</option>
                            <option>9:30pm</option>
                            <option>10:00pm</option>
                            <option>10:30pm</option>
                            <option>11:00pm</option>
                        </select>
                    </label>
                    <label>Fecha<span>(Mayo)</span>
                        <select>
                            <option>1</option>
                            <option>3</option>
                            <option>5</option>
                            <option>6</option>
                            <option>7</option>
                            <option>11</option>
                            <option>12</option>
                            <option>15</option>
                            <option>17</option>
                            <option>22</option>
                            <option>23</option>
                            <option>26</option>
                        </select>
                    </label>
                    <label>Mesa
                        <select>
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                            <option>6</option>
                            <option>7</option>
                            <option>8</option>
                            <option>9</option>
                            <option>10</option>
                            <option>11</option>
                        </select>
                    </label>
                    <label>Cantidad de personas
                        <select>
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                            <option>6</option>
                            <option>7</option>
                            <option>8</option>
                            <option>9</option>
                        </select>
                    </label>
                    <label>Tipo de Reserva
                        <select>
                            <option>Regular</option>
                            <option>Royal</option>
                        </select>
                    </label>
                </fieldset>
                <fieldset>
                    <legend>Compra</legend>
                    <label>Metodo de pago
                    <input type="text"></label>
                    <label>Propina<span>(A voluntad)</span>
                    <input type="text"></label>
                </fieldset>
            </form>
        </main>
        
    </body>
</html>