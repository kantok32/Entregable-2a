import gradio as gr
from huggingface_hub import InferenceClient
import os

# Obtén el token de manera segura desde el entorno
hf_token = os.getenv("HF_API_TOKEN")
client = InferenceClient(
    "microsoft/Phi-3-mini-4k-instruct",
    token=hf_token
)

# Define la función de inferencia que usa la API
def generate_response(input_text):
    prompt = f"Debes de responder a cualquier pregunta:\nPregunta: {input_text}"
    try:
        # Realizar la inferencia usando el cliente de Hugging Face
        messages = [{"role": "user", "content": prompt}]
        response = client.chat_completion(messages=messages, max_tokens=500)
        
        # Extrae el texto generado
        if hasattr(response, 'choices') and response.choices:
            generated_text = response.choices[0].message.content
        else:
            generated_text = str(response)
            
        return generated_text
    except Exception as e:
        return f"Error al realizar la inferencia: {e}"

# Configura la interfaz en Gradio con un diseño más interactivo
with gr.Blocks(title="LLM Chatbot con API de Inferencia") as demo:
    gr.Markdown(
        """
        ## Chatbot LLM - Pregunta y Respuesta
        Este chatbot utiliza un modelo de lenguaje para responder preguntas. 
        Ingresa tu consulta en el área de texto a continuación y presiona el botón de enviar para obtener una respuesta.
        """
    )
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                lines=5,
                placeholder="Escribe tu pregunta aquí...",
                label="Pregunta"
            )
        with gr.Column():
            output_text = gr.Textbox(
                lines=5,
                label="Respuesta",
                interactive=False
            )
    submit_button = gr.Button("Enviar")
    
    # Conecta la función a los componentes
    submit_button.click(fn=generate_response, inputs=input_text, outputs=output_text)

# Lanza la interfaz
demo.launch()