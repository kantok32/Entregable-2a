
# Proyecto 1: Chatbot LLM con API de Hugging Face

## 📋 Descripción
Este proyecto es un chatbot interactivo que utiliza un modelo de lenguaje de Hugging Face para responder preguntas en tiempo real. La aplicación está construida con Gradio, lo que permite al usuario interactuar fácilmente con el modelo a través de una interfaz gráfica.

---

## 📦 Requisitos
Antes de ejecutar este proyecto, asegúrate de tener lo siguiente instalado en tu equipo:
- **Python 3.8 o superior**
- **Gradio**
- **huggingface_hub**

Instala las dependencias ejecutando:
```bash
pip install gradio huggingface_hub
```

---

## 🔐 Configuración del Token de Hugging Face
El proyecto requiere un **token de acceso** de Hugging Face para conectarse a la API del modelo.

### Cómo Obtener un Token
1. Inicia sesión en tu cuenta de Hugging Face:  
   👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Crea un nuevo token con los siguientes permisos habilitados:
   - **`Read`** (lectura)
3. Copia el token generado.

### Configura el Token como Variable de Entorno
Para mantener tu token seguro, configúralo como una variable de entorno en tu sistema:

- **Windows (PowerShell):**
   ```powershell
   $env:HF_API_TOKEN="TU_TOKEN"
   ```

- **Linux/macOS:**
   ```bash
   export HF_API_TOKEN="TU_TOKEN"
   ```

---

## 🚀 Cómo Ejecutar el Archivo
1. Guarda el código en un archivo llamado **`app.py`**.
2. Abre la terminal en la carpeta donde guardaste el archivo.
3. Ejecuta el archivo con el siguiente comando:

```bash
python app.py
```

4. Abre el navegador y visita la URL proporcionada (por defecto: `http://127.0.0.1:7860`).

---

## 📚 Modelo Usado
- **Modelo:** `microsoft/Phi-3-mini-4k-instruct`
- **Fuente:** Hugging Face

El modelo está diseñado para responder preguntas en lenguaje natural.

---

## 📤 Parámetros en la Petición
La aplicación realiza peticiones a la API de Hugging Face utilizando los siguientes parámetros:
- **`messages`**: Lista de mensajes en formato JSON. Ejemplo:
  ```json
  [
    {"role": "user", "content": "¿Cuál es la capital de Francia?"}
  ]
  ```
- **`max_tokens`**: Número máximo de tokens en la respuesta (500).

---

## ✨ Ejemplo de Uso
1. Ingresa una pregunta en el cuadro de texto, por ejemplo:
   ```text
   ¿Cuál es la capital de Francia?
   ```
2. Presiona el botón **"Enviar"**.
3. La respuesta generada será:
   ```text
   La capital de Francia es París.
   ```

---

## ⚙️ Instalación Opcional (Entorno Virtual)
Para mantener las dependencias aisladas, puedes crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
.env\Scriptsctivate  # En Windows
```

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT.

