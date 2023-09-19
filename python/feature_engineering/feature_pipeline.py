# Own libraries
from python.feature_engineering.utils.filters import clean_text, create_df
from python.metadata.path import Path
from python.utils.readers import read_yaml


def executor():
    text_yml = read_yaml(Path.text)

    data = create_df(text=text_yml['text'])

    data = clean_text(df=data, column='text')

    return data
