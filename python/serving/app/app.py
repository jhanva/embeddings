# External libraries
import gradio as gr
import numpy as np

# Own libraries
from python.serving.app.utils.filters import question_answer


def app(sentence: str) -> np.array:
    """

    Args:
        sentence:

    Returns:

    """
    answer = question_answer(sentence)
    return answer


def run_demo():
    demo = gr.Interface(
        fn=app,
        inputs=gr.Textbox(
            lines=5, placeholder='Enter question from LOTR in Spanish'
        ),
        outputs=gr.Textbox(lines=5),
        live=True,
    )

    demo.launch()
