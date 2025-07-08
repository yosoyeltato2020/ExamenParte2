###
Explicacion: 
Se crea una app.py de la aplicación Flask, utilizando este framework flask... lo que permite configurar 
un entorno de desarrollo, 
- Se define un endpoint `/saludo/<nombre>` que acepta solicitudes GET.
- La función `saludo` toma el parámetro `nombre` de la URL y devuelve un JSON con un mensaje de saludo.
- Se utiliza el método `jsonify` para devolver un JSON con el mensaje.

Ejecución:
   Bueno, mi querido profesor...te dejo el requirements.txt por si acaso.
   pero tienes que instalar flask 
1. Instala Flask utilizando pip: `pip install flask`
2. Guarda el código en un archivo llamado `app.py`
3. Ejecuta la aplicación con `python app.py`
4. Accede al endpoint en `http://localhost:5000/saludo/tu_nombre` para ver el mensaje de saludo.
###

