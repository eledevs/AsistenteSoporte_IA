# 🎀 Asistente Virtual de Soporte Técnico (IA y Big Data)

Este proyecto ha sido desarrollado como el **Trabajo de Enfoque** para el módulo de Modelos de Inteligencia Artificial. [cite_start]Consiste en un asistente virtual interactivo diseñado para brindar soporte técnico automatizado en una empresa de servicios tecnológicos[cite: 19].

## 🚀 Funcionalidades
- [cite_start]**Procesamiento de Lenguaje Natural (PLN):** Implementación de la librería **spaCy** para interpretar consultas en lenguaje natural[cite: 22, 49].
- [cite_start]**Diagnóstico en Tiempo Real:** Capacidad para resolver dudas sobre conectividad, acceso a cuentas y mantenimiento de hardware[cite: 31].
- [cite_start]**Interfaz Web "Coquette":** Frontend interactivo desarrollado con HTML/CSS orientado a una experiencia de usuario amigable y profesional[cite: 57, 93].
- [cite_start]**API REST:** Backend robusto utilizando **Flask** para el despliegue del servicio[cite: 56].

## 🛠️ Requisitos del Sistema
[cite_start]Para el correcto funcionamiento en entornos macOS (especialmente MacBook Air), se requiere[cite: 240]:
- **Python 3.10** o superior.
- Librerías necesarias: `flask`, `spacy`, `scikit-learn`.
- Modelo de lenguaje español: `es_core_news_sm`.

## ⚙️ Instalación y Uso
1. **Instalar dependencias:**
   ```bash
   pip3 install flask spacy scikit-learn
   python3 -m spacy download es_core_news_sm
   ```
2. **Ejecutar la aplicación:**
    ```bash
   python3 app.py
   ```
4. **Acceso:**
Abrir el navegador en
 ```bash
   http://127.0.0.1:5001
   ```
(Puerto configurado para evitar conflictos de sistema en Mac).

## ⚖️ Consideraciones Éticas y Legales
El desarrollo sigue estrictamente los principios de "Privacy by Design". Se garantiza la privacidad de los datos de los usuarios y el cumplimiento de las normativas vigentes sobre transparencia en la Inteligencia Artificial. El uso de la IA se ha tomado como vehículo potenciador del aprendizaje y no como sustitutivo del conocimiento.
