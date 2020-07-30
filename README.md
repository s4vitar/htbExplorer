# htbExplorer

**htbExplorer** es un cliente de terminal hecho en Bash ideal para trabajar cómodamente desde consola sobre la plataforma de HackTheBox.

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

La utilidad **htbExplorer** cuenta con múltiples opciones:

<p align="center">
<img src="Images/fifth.png"
        alt="Fifth"
        style="float: left; margin-right: 10px;" />
</p>

Una de ellas, es el modo de exploración. Para hacer uso de este modo, a través del parámetro '**-e**', podemos indicar el modo de exploración que queremos realizar. 

Por ejemplo, para listar las máquinas activas, haríamos '**-e active_machines**', obteniendo los siguientes resultados:

<p align="center">
<img src="Images/6.png"
        alt="6"
        style="float: left; margin-right: 10px;" />
</p>

O por el contrario, para listar las máquinas spawneadas, haríamos '**-e spawned_machines**', entre los otros 14 modos de exploración (es bastante intuitivo y sencillo de usar):

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

De igual manera, podemos encontrar las máquinas proporcionando la dirección IP de estas:

<p align="center">
<img src="Images/9.png"
        alt="9"
        style="float: left; margin-right: 10px;" />
</p>

A través del parámetro '**-r**', tenemos la capacidad de reiniciar una máquina en base al nombre de máquina que especifiquemos, debiendo esperar 1 minuto para poder reiniciar otra de las activas:

<p align="center">
<img src="Images/10.png"
        alt="10"
        style="float: left; margin-right: 10px;" />
</p>

Asimismo, es posible desplegar una nueva máquina del LAB (siempre y cuando seas VIP), haciendo uso para ello del parámetro '**-d**':

<p align="center">
<img src="Images/11.png"
        alt="11"
        style="float: left; margin-right: 10px;" />
</p>

En caso de querer extender el tiempo de una máquina, o parar aquella máquina que hayamos desplegado, se puede hacer uso de los parámetros '**-x**' y '**-k**' respectivamente:

<p align="center">
<img src="Images/12.png"
        alt="12"
        style="float: left; margin-right: 10px;" />
</p>

Dado que solo podemos extender el tiempo en aquella máquina de la cual seamos propietarios, para asignarte como propietario de una máquina, puedes hacer uso del parámetro '**-a**'. De esta forma, posteriormente, podrás extender su tiempo de vida a 24 horas:

<p align="center">
<img src="Images/13.png"
        alt="13"
        style="float: left; margin-right: 10px;" />
</p>

**htbExplorer** cuenta con un buscador de usuarios, representando la información más relevante de estos en tablas:

<p align="center">
<img src="Images/14.png"
        alt="14"
        style="float: left; margin-right: 10px;" />
</p>

¿Quieres saber lo que se está hablando en el ShoutBox?, a través del parámetro '**-c**', puedes indicar el número de mensajes a cargar, pudiendo así ver toda la actividad:

<p align="center">
<img src="Images/15.png"
        alt="15"
        style="float: left; margin-right: 10px;" />
</p>

¿Eres un curioso y te gustaría saber quiénes están hablando?, no te preocupes, con el parámetro '**-w**', podrás representar la información más relevante de aquellos usuarios que estén hablando o generando actividad (siempre y cuando tengan el perfil público). También es necesario indicar el número de mensajes a cargar:

<p align="center">
<img src="Images/16.png"
        alt="16"
        style="float: left; margin-right: 10px;" />
</p>

En caso de querer descargarte la VPN, ya no es necesario abrir el navegador. A través del parámetro '**-v**', podrás descargar tu VPN cómodamente indicando para ello un nombre de exportación:

<p align="center">
<img src="Images/17.png"
	alt="17"
    style="float: left; margin-right: 10px;" />
</p>
                                

TODO
======
* Poder hacer submit de una flag desde htbExplorer
* Indicar si eres propietario de alguna máquina, obteniendo el nombre de esta

