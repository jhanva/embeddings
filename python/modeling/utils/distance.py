# External libraries
import numpy as np
import pandas as pd


def find_closest_sentences(
    input_vector: np.array, df: pd.DataFrame, column_name: str, topn: int = 1
) -> pd.Series:
    """Finds the closest rows in a DataFrame with embeddings to a given input
        vector based on Euclidean distance.

    Args:
        input_vector: The input vector for comparison.
        df: The DataFrame containing embeddings to compare against.
        column_name: The name of the column containing embeddings in the
            DataFrame.
        topn: The number of closest rows to retrieve (default is 1).

    Returns:
        A DataFrame containing the 'topn' closest rows based on Euclidean
            distance.

    """
    df['distance'] = df.apply(
        lambda row: np.linalg.norm(input_vector - row[column_name]), axis=1
    )
    closest_rows = df.nsmallest(topn, 'distance')

    return closest_rows['text'].values
