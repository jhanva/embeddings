# Own libraries
from python.feature_engineering import feature_pipeline
from python.modeling.utils.embeddings import train_model


def executor():
    data = feature_pipeline.executor()
    print('here')
    data = train_model(data, save=True)

    print(data)
