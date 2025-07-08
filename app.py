# Hola Profe,,, pues esto es un ejemplo de un servicio web ligero...que implementa un endpoind.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo/<ismael>', methods=['GET'])
def saludo(nombre):
    mensaje = f'Hola {nombre}'
    return jsonify({'mensaje': mensaje})

if __name__ == '__main__':
    app.run

    
"""
Explicacion: 
Se crea una app.py de la aplicación Flask, utilizando este framework flask... lo que permite configurar 
un entorno de desarrollo, 
- Se define un endpoint `/saludo/<nombre>` que acepta solicitudes GET.
- La función `saludo` toma el parámetro `nombre` de la URL y devuelve un JSON con un mensaje de saludo.
- Se utiliza el método `jsonify` para devolver un JSON con el mensaje.

Ejecución:
   Bueno, mi querido profesor...te dejo el requirements.txt por si acaso.
   pero tienes que instalar 

"""





