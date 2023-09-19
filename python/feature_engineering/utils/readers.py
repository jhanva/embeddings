# External libraries
import yaml


def read_yaml(path: str) -> dict:
    """Reads and parses YAML data from a specified file.

    Args:
        path: The path to the YAML file to be read.

    Returns:
        A dictionary containing the parsed YAML data.

    """
    with open(path, encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data
