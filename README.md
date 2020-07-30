# htbExplorer

**htbExplorer** es una herramienta ideal para trabajar cómodamente desde consola sobre la plataforma de HackTheBox.

¿Cómo ejecuto la herramienta?
======
Para empezar, tras ejecutar la herramienta, veremos lo siguiente:

<p align="center">
<img src="Images/first.png"
        alt="First"
        style="float: left; margin-right: 10px;" />
</p>

Esto es así dado que en primer lugar, necesitamos proporcionar nuestra API Key de HackTheBox.

Para ello, iniciaremos sesión en el panel de HackTheBox. Una vez logueados, haremos click derecho en nuestro perfil y posteriormente nos iremos a '**Settings**'. Dentro de esta pestaña, podremos ver un apartado con nombre '**API KEY**', desde donde podremos visualizar nuestra API Key (valga la redundancia):

<p align="center">
<img src="Images/second.png"
        alt="Second"
        style="float: left; margin-right: 10px;" />
</p>

Ya en tenencia de esta API Key, es necesario introducirla en esta porción del código:

<p align="center">
<img src="Images/third.png"
        alt="Third"
        style="float: left; margin-right: 10px;" />
</p>

Una vez introducida, podremos ejecutar la aplicación. Tras su ejecución, veremos el siguiente panel:

<p align="center">
<img src="Images/fourth.png"
        alt="Fourth"
        style="float: left; margin-right: 10px;" />
</p>

El cual cuenta con múltiples opciones:

<p align="center">
<img src="Images/fifth.png"
        alt="Fifth"
        style="float: left; margin-right: 10px;" />
</p>

Para hacer uso del modo de exploración, a travésd el parámetro '**-e**' podremos indicar el modo de exploración que queremos realizar. Por ejemplo, para listar las máquinas activas:

<p align="center">
<img src="Images/6.png"
        alt="6"
        style="float: left; margin-right: 10px;" />
</p>

O por el contrario, para listar las máquinas spawneadas:

<p align="center">
<img src="Images/7.png"
        alt="7"
        style="float: left; margin-right: 10px;" />
</p>

La utilidad **htbExplorer** cuenta con un buscador de máquinas por palabras clave, de forma que en todo momento podemos extraer la información más relevante de una máquina, aún sin saber su nombre entero:

<p align="center">
<img src="Images/8.png"
        alt="8"
        style="float: left; margin-right: 10px;" />
</p>
