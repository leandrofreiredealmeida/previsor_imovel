import joblib
import os
import yaml # For parsing YAML files
from src.previsor import logger
import json
import joblib # For saving and loading Python objects
from ensure import ensure_annotations # For runtime validation of type hints
from box import ConfigBox # For accessing dictionary values like attributes
from pathlib import Path # For file path operations
from typing import Any
from box.exceptions import BoxValueError # Exception specific to Box operations

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads YAML file and returns ConfigBox object

    Args:
        path_to_yaml (Path): path-like input (expects a Path object)

    Raises:
        ValueError: if yaml file is empty
        e: propagates any other exception
        
    Returns:
        ConfigBox: ConfigBox type object containing the YAML data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 

@ensure_annotations
def save_json(path: Path, data: dict):
    """ save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ load json files data
    
    Args:
        path (Path): path to json file
        
    Returns:
        ConfigBox: ConfigBox type object containing the json data
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
        
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ save binary data
    
    Args:
        data (Any): data to be saved in binary file
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """ load binary data
    
    Args:
        path (Path): path to binary file
        
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded succesfully from: {path}")
    return data
  
        