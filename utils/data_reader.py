import json, os
from dotenv import load_dotenv
from typing import Dict, Any


def read_json(file_path: str) -> Dict[str, Any]:
    """ Read a JSON file and return a dictionary """
    with open(file_path, "r") as file:
        return json.load(file)
    

def get_checkout_data() -> Dict[str, Any]:
    """ Get the checkout data from the JSON file """
    file_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "checkout_data.json")
    return read_json(file_path)


def get_test_validation_data() -> Dict[str, Any]:
    """ Get the test validation data from the JSON file """
    file_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "test_validation_data.json")
    return read_json(file_path)


def get_environment_data() -> Dict[str, Any]:
    """ Get the environment data from the .env file """
    # Load .env from the project root
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
    env_dict: Dict[str, Any] = {
        "base_url": os.getenv("BASE_URL"),
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
    return env_dict

