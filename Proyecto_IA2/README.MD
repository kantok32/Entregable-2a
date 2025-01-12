 🧠 README: Multi-Model LLM Chatbot with Image Generation and Emotion Analysis
📋 Descripción del Proyecto
Este proyecto es un Chatbot Multi-Modelo interactivo que utiliza modelos alojados en Hugging Face para:

Responder preguntas utilizando un modelo LLM (Language Learning Model).
Recordar el historial de conversación para proporcionar respuestas más coherentes.
Analizar emociones en los textos proporcionados por los usuarios.
Generar imágenes a partir de descripciones de texto utilizando un modelo ligero y eficiente.
El proyecto está construido con Gradio para proporcionar una interfaz gráfica interactiva y fácil de usar.

📦 Requisitos Previos
Antes de ejecutar este proyecto, asegúrate de tener lo siguiente instalado en tu máquina:

Python 3.8 o superior
Git
Dependencias del proyecto:
gradio
huggingface_hub
Instala las dependencias ejecutando:

bash
Copiar código
pip install -r requirements.txt
🔐 Configuración del Token de Hugging Face
Este proyecto utiliza modelos alojados en Hugging Face, por lo que necesitas un token de acceso para usarlos.

📋 Cómo Obtener un Token de Acceso
Inicia sesión en Hugging Face.
Genera un token de lectura.
Configura el token como variable de entorno en tu máquina:
Linux/macOS:
bash
Copiar código
export HF_API_TOKEN="TU_TOKEN"
Windows (PowerShell):
powershell
Copiar código
$env:HF_API_TOKEN="TU_TOKEN"
🚀 Instrucciones para Ejecutar el Proyecto
1️⃣ Clona el Repositorio
bash
Copiar código
git clone https://huggingface.co/tu_usuario/tu_repositorio
cd tu_repositorio
2️⃣ Instala las Dependencias
bash
Copiar código
pip install -r requirements.txt
3️⃣ Ejecuta la Aplicación
bash
Copiar código
python app.py
4️⃣ Abre la Interfaz en tu Navegador
La aplicación estará disponible en http://127.0.0.1:7860.

🧩 Diagrama de Flujo del Chatbot
El siguiente diagrama de flujo muestra cómo el chatbot selecciona el modelo adecuado y procesa la entrada del usuario:

mermaid
Copiar código
flowchart TD
    Start["Usuario ingresa una consulta"] --> SelectModel{¿Selecciona acción?}
    SelectModel -- "CHATBOT" --> LLMResponse["Respuesta generada por el modelo LLM"]
    SelectModel -- "Generar Imagen" --> ImageResponse["Generación de imagen en progreso"]
    SelectModel -- "Análisis de Emociones" --> EmotionResponse["Análisis de emociones en el texto"]
    LLMResponse --> End["Respuesta devuelta al usuario"]
    ImageResponse --> End
    EmotionResponse --> End

    Ejemplo de Uso
   En la carpeta assets se encuentran capturas de prueba de los 3 modelos utilizados

    
⚙️ Instalación Opcional: Uso de un Entorno Virtual
Para mantener las dependencias aisladas y evitar conflictos, puedes crear un entorno virtual con los siguientes comandos:

Linux/macOS:
bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Windows:
bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
✅ Modelos Utilizados
microsoft/Phi-3-mini-4k-instruct – Modelo de lenguaje para responder preguntas y recordar el contexto de la conversación.
bhadresh-savani/distilbert-base-uncased-emotion – Modelo para análisis de emociones.
stabilityai/stable-diffusion-2-1-base – Modelo ligero para generación de imágenes.
📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente bajo los términos de esta licencia.

