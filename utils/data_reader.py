import json
import os
import logging
from dotenv import load_dotenv
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def read_json(file_path: str) -> Dict[str, Any]:
    """Read a JSON file and return a dictionary."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            logger.info(f"Successfully loaded JSON file: {file_path}")
            return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {file_path}: {e}")
        raise

def get_checkout_data() -> Dict[str, Any]:
    """Get the checkout data from the JSON file."""
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "checkout_data.json")
    return read_json(file_path)

def get_test_validation_data() -> Dict[str, Any]:
    """Get the test validation data from the JSON file."""
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "test_validation_data.json")
    return read_json(file_path)

def get_environment_data() -> Dict[str, Any]:
    """Get environment data from the .env file."""
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if not os.path.exists(env_path):
        logger.warning(f".env file not found at {env_path}")

    load_dotenv(env_path)

    env_dict = {
        "base_url": os.getenv("BASE_URL"),
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }

    if not all(env_dict.values()):
        logger.warning("Some environment variables are missing or empty.")

    return env_dict
