# Hola Profe,,, pues esto es un ejemplo de un servicio web ligero...que implementa un endpoind.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo/<nombre>', methods=['GET'])
def saludo(nombre):
    mensaje = f'Hola {nombre}'
    return jsonify({'mensaje': mensaje})

if __name__ == '__main__':
    app.run()







