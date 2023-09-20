# Own libraries
from python.feature_engineering import feature_pipeline
from python.metadata.path import Path
from python.modeling import modeling_pipeline
from python.serving.app.app import run_demo
from python.utils.readers import read_yaml

if __name__ == '__main__':
    config = read_yaml(Path.config)
    model = config['pipeline']

    if model == 'train':
        feature_pipeline.executor(config[model]['feature_pipeline']['save'])
        modeling_pipeline.executor(config[model]['modeling_pipeline']['save'])

    elif model == 'eval':
        run_demo()

    else:
        raise NotImplementedError
