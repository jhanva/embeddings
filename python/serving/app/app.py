# External libraries
import gradio as gr

# Own libraries
from python.serving.app.utils.filters import question_answer


def app(sentence):
    return question_answer(sentence)


def interface():
    demo = gr.Interface(fn=app, inputs="text", outputs="text")
    demo.launch()
