import spacy
from flask import Flask, render_template, request, jsonify
from datos import preguntas_frecuentes

app = Flask(__name__)

try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    nlp = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    datos = request.get_json()
    if not datos or 'mensaje' not in datos:
        return jsonify({"asistente": "¡Oh no! No he recibido tu mensaje correctamente. 🎀"}), 400

    mensaje_usuario = datos.get("mensaje", "").lower()
    
    # Busca si alguna palabra clave de 'datos.py' está en el mensaje
    respuesta = "No estoy segura de cómo ayudarte con eso, linda. ¿Podrías darme más detalles? ✨"
    
    # Mapeo de palabras clave para que el bot sea más flexible
    mapeo = {
        "internet": "red", "wifi": "red", "conector": "red",
        "contraseña": "acceso", "clave": "acceso", "password": "acceso",
        "encender": "hardware", "prende": "hardware", "luz": "hardware",
        "lento": "lento", "rapido": "lento", "memoria": "lento",
        "impresora": "impresora", "papel": "impresora", "tinta": "impresora",
        "correo": "correo", "email": "correo", "outlook": "correo",
        "instalar": "software", "programa": "software", "aplicacion": "software"
    }

    # Revisamos el mensaje del usuario
    for palabra_clave, categoria in mapeo.items():
        if palabra_clave in mensaje_usuario:
            respuesta = preguntas_frecuentes[categoria]
            break # En cuanto encuentra una, responde
        
    return jsonify({"asistente": respuesta})

if __name__ == "__main__":
    app.run(debug=True, port=5001)