# External libraries
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Own libraries
from python.metadata.path import Path
from python.utils.readers import read_yaml


def encode_model(arr: np.array) -> np.array:
    """Generates text embeddings for a DataFrame column using a pre-trained
        NLP model.

    Args:
        arr: A NumPy array containing text data.

    Returns:
        np.ndarray: An array of text embeddings for the specified column.

    """
    model_yml = read_yaml(Path.config)

    model = SentenceTransformer(model_yml['embedding_model'])

    embeddings = model.encode(
        arr, batch_size=model_yml['batch_size'], show_progress_bar=True
    )

    return embeddings


def train_model(df: pd.DataFrame, save: bool = False) -> pd.DataFrame:
    """Trains a model or generates embeddings from text data in a DataFrame.

    Args:
        df: The DataFrame containing the text data in the 'text' column.
        save:

    Returns:
        The input DataFrame with additional 'embeddings' and 'ids' columns.

    """
    embeddings = encode_model(np.array(df['text_embedding']))

    df['embeddings'] = embeddings.tolist()
    df['ids'] = df.index
    df['ids'] = df['ids'].astype(str)

    if save:
        df.to_parquet(Path.output_model, index=False)

    return df
