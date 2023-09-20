# External libraries
import re

import nltk
import pandas as pd
from gensim.parsing.preprocessing import (
    strip_numeric,
    strip_punctuation,
    strip_short,
)
from nltk.corpus import stopwords

# Own libraries
from python.metadata.path import Path


def create_df(text: str) -> pd.DataFrame:
    """Creates a DataFrame from a long text, splitting it into sentences.

    Args:
        text: The input text to be split into sentences.

    Returns:
        A DataFrame with a single column 'text' containing the extracted
            sentences.

    """
    texts = text.split('. ')

    df = pd.DataFrame({'text': texts})

    return df


def clean_text(
    df: pd.DataFrame, column: str, save: bool = False
) -> pd.DataFrame:
    """Cleans and preprocesses text data in a specified DataFrame column.

    Args:
        df: The DataFrame containing the text data.
        column: The name of the column to be cleaned.
        save: option to save data.

    Returns:
        A DataFrame with the specified column cleaned and preprocessed.

    """
    # Download the stopwords if not already downloaded
    nltk.download('stopwords')

    # Get the Spanish stopwords
    stop_words = set(stopwords.words('spanish'))

    # Initialize a list to store cleaned words
    list_words = []

    # Iterate through each string in the specified column
    for string in df[column]:
        string = string.lower()

        # Remove numbers
        string = re.sub(r'\d+', '', string)

        # Remove URLs, links, and mentions
        string = re.sub(
            r'http\S+|www\S+|https\S+|\@\w+|\#\w+',
            '',
            string,
            flags=re.MULTILINE,
        )

        string = string.replace('\n', '')

        # Remove punctuation
        string = strip_punctuation(string)

        # Remove numbers
        string = strip_numeric(string)

        # Remove sort words
        string = strip_short(string, minsize=2)

        # Split the string into words
        words = string.split()

        # Filter out stopwords
        words_stopwords = [word for word in words if word not in stop_words]

        # Join the cleaned words back into a string
        clean_word = ' '.join(words_stopwords)

        # Append the cleaned string to the list
        list_words.append(clean_word)

    # Update the DataFrame column with the cleaned text
    df[f'{column}_embedding'] = list_words

    cond_length = df[f'{column}_embedding'].apply(lambda x: len(x.split()))
    df = df[cond_length > 3]

    if save:
        df.to_parquet(Path.clean_data, index=False)

    return df
