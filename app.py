from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: Prueba de estado (Health Check)
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "Éxito",
        "mensaje": "¡Hola desde AWS EC2! La API está funcionando correctamente."
    }), 200

# Endpoint 2: Prueba de datos (Simulación de una consulta)
@app.route('/datos', methods=['GET'])
def obtener_datos():
    datos_simulados = [
        {"id": 1, "nombre": "Instancia EC2", "os": "Ubuntu"},
        {"id": 2, "nombre": "Manejo e Implementación de Archivos", "curso": "MIA"}
    ]
    return jsonify({
        "status": "Éxito",
        "data": datos_simulados
    }), 200

if __name__ == '__main__':
    # Configurar el host en '0.0.0.0' permite que la API reciba peticiones externas.
    # El puerto 5000 es el puerto por defecto de Flask.
    app.run(host='0.0.0.0', port=5000, debug=True)