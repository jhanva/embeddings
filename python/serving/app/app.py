# External libraries
import gradio as gr
import numpy as np

# Own libraries
from python.serving.app.utils.filters import question_answer


def app(sentence: str) -> np.array:
    """Answer a question based on the input sentence.

    Args:
        sentence: The input sentence or question.

    Returns:
        An array containing the answer or response.

    """
    answer = question_answer(sentence)
    return answer


def run_demo() -> None:
    """Run a Gradio demo for the question-answering application.

    This function creates a Gradio interface for the 'app' function, allowing
        users to input questions and receive answers.

    """
    demo = gr.Interface(
        fn=app,
        inputs=gr.Textbox(
            lines=5, placeholder='Enter question from LOTR in Spanish'
        ),
        outputs=gr.Textbox(lines=5),
        live=False,
        title='Q&A Lord of the ring',
    )

    demo.launch()
