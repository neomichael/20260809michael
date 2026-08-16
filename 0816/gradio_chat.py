from google import genai
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.5-flash"


def chat(message, history):
    interaction = client.interactions.create(
        model=MODEL,
        input=message,
    )
    return interaction.output_text


demo = gr.ChatInterface(fn=chat, title="Gemini 聊天機器人")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
