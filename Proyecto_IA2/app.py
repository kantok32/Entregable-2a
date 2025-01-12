import gradio as gr
from huggingface_hub import InferenceClient
import os
import time

# Obtén el token de manera segura desde el entorno
hf_token = os.getenv("HF_API_TOKEN")

# Clase para manejar múltiples modelos
class ModelHandler:
    def __init__(self, model_names, token):
        self.clients = {model_key: InferenceClient(model_name, token=token) for model_key, model_name in model_names.items()}
        self.current_model = list(model_names.keys())[0]
        self.conversation_history = []  # Memoria de conversación

    def switch_model(self, model_key):
        if model_key in self.clients:
            self.current_model = model_key
        else:
            raise ValueError(f"Modelo {model_key} no está disponible.")

    def generate_response(self, input_text):
        # Agrega el historial de la conversación al prompt
        self.conversation_history.append({"role": "user", "content": input_text})
        prompt = f"Historial de conversación: {self.conversation_history}\nPregunta: {input_text}"
        
        try:
            messages = [{"role": "user", "content": prompt}]
            client = self.clients[self.current_model]
            response = client.chat_completion(messages=messages, max_tokens=500)
            if hasattr(response, 'choices') and response.choices:
                generated_text = response.choices[0].message.content
                self.conversation_history.append({"role": "assistant", "content": generated_text})
                return generated_text
            else:
                return str(response)
        except Exception as e:
            return f"Error al realizar la inferencia: {e}"

    def analyze_emotion(self, input_text):
        # Diccionario para traducir emociones al español
        emotion_translation = {
            "joy": "Alegría",
            "anger": "Enojo",
            "fear": "Miedo",
            "sadness": "Tristeza",
            "love": "Amor",
            "surprise": "Sorpresa"
        }
        
        try:
            client = InferenceClient("bhadresh-savani/distilbert-base-uncased-emotion", token=hf_token)
            response = client.text_classification(input_text)
            
            # Traducir las emociones y formatear la respuesta
            emotions = [
                f"{emotion_translation[label['label']]}: {label['score']:.2%}"
                for label in response
            ]
            return "\n".join(emotions)
        except Exception as e:
            return f"Error al analizar la emoción: {e}"

# Lista de modelos disponibles (con nombres amigables para la interfaz)
model_names = {
    "CHATBOT": "microsoft/Phi-3-mini-4k-instruct"
}

# Inicializa el manejador de modelos
model_handler = ModelHandler(model_names, hf_token)

# Define la función para generación de imágenes con progreso utilizando un tiempo de espera ilimitado
def generate_image_with_progress(prompt):
    try:
        client = InferenceClient("stabilityai/stable-diffusion-2-1-base", token=hf_token, timeout=None)

        # Simular progreso
        for progress in range(0, 101, 20):
            time.sleep(0.5)
            yield f"Generando imagen... {progress}% completado", None

        image = client.text_to_image(prompt, width=512, height=512)
        yield "Imagen generada con éxito", image
    except Exception as e:
        yield f"Error al generar la imagen: {e}", None

# Configura la interfaz en Gradio con selección de modelos y generación de imágenes
with gr.Blocks(title="Multi-Model LLM Chatbot with Image Generation and Emotion Analysis") as demo:
    gr.Markdown(
        """
        ## Chatbot Multi-Modelo LLM con Generación de Imágenes y Análisis de Emociones
        Este chatbot permite elegir entre múltiples modelos de lenguaje para responder preguntas, recordar la conversación o analizar emociones en los textos.
        """
    )
    with gr.Row():
        model_dropdown = gr.Dropdown(
            choices=list(model_names.keys()) + ["Generación de Imágenes", "Análisis de Emociones"],
            value="CHATBOT",
            label="Seleccionar Acción/Modelo",
            interactive=True
        )
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                lines=5,
                placeholder="Escribe tu consulta o descripción para la imagen...",
                label="Entrada"
            )
        with gr.Column():
            output_display = gr.Textbox(
                lines=5,
                label="Estado",
                interactive=False
            )
            output_image = gr.Image(
                label="Imagen Generada",
                interactive=False
            )
    submit_button = gr.Button("Enviar")

    # Define la función de actualización
    def process_input(selected_action, user_input):
        try:
            if selected_action == "Generación de Imágenes":
                progress_generator = generate_image_with_progress(user_input)
                last_status = None
                last_image = None
                for status, image in progress_generator:
                    last_status = status
                    last_image = image
                return last_status, last_image
            elif selected_action == "Análisis de Emociones":
                emotion_result = model_handler.analyze_emotion(user_input)
                return f"Emoción detectada:\n{emotion_result}", None
            else:
                model_handler.switch_model(selected_action)
                response = model_handler.generate_response(user_input)
                return response, None
        except Exception as e:
            return f"Error: {e}", None

    # Conecta la función a los componentes
    submit_button.click(
        fn=process_input,
        inputs=[model_dropdown, input_text],
        outputs=[output_display, output_image]
    )

# Lanza la interfaz
demo.launch()
