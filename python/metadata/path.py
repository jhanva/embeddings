# External libraries
import os


class Path:
    """object to store structures."""

    clean_data = os.path.join('output', 'clean_data', 'text.parquet')

    features_model = os.path.join('output', 'feature_store', 'text.parquet')

    config = os.path.join('input', 'setting', 'config.yaml')

    text = os.path.join('input', 'text.yaml')
