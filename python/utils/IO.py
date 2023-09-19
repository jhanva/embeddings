# External libraries
import numpy as np

# Own libraries
from python.modeling.utils.embeddings import encode_model


def enter_question(sentence: str) -> np.array:
    """Encodes a user-entered question into an embedding.

    Args:
        sentence (str): The user-entered question or sentence.

    Returns:
        np.ndarray: An array representing the embedding of the input sentence.

    """
    sentence_arr = np.array([sentence])

    query_embedding = encode_model(sentence_arr)

    return query_embedding[0]
