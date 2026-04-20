import spacy
from datos import preguntas_frecuentes

# motor de lenguaje 
nlp = spacy.load("es_core_news_sm")

def chatbot():
    print("Hola, soy tu asistente de soporte técnico. ¿En qué puedo ayudarte? (Escribe 'salir' para terminar)")
    
    while True:
        entrada = input("\nUsuario: ").lower()
        if entrada == "salir":
            break
            
        # La IA analiza la frase
        doc = nlp(entrada)
        
        # búsqueda de palabras clave
        encontrado = False
        if "internet" in entrada or "wifi" in entrada:
            print("Asistente:", preguntas_frecuentes["red"])
            encontrado = True
        elif "contraseña" in entrada or "clave" in entrada:
            print("Asistente:", preguntas_frecuentes["acceso"])
            encontrado = True
        elif "encender" in entrada or "luz" in entrada:
            print("Asistente:", preguntas_frecuentes["hardware"])
            encontrado = True
            
        if not encontrado:
            print("Asistente: No estoy seguro de cómo ayudarte con eso. ¿Podrías ser más específico?")

if __name__ == "__main__":
    chatbot()