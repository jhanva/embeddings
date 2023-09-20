# External libraries
import pandas as pd

# Own libraries
from python.metadata.path import Path
from python.modeling.utils.embeddings import train_model


def executor(save: bool) -> pd.DataFrame:
    """Execute the modeling pipeline."""

    data = pd.read_parquet(Path.clean_data)

    data = train_model(data, save=save)

    print('Modeling pipeline finished!')
    return data
