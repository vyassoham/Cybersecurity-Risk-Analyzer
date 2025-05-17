import datetime
import json
import os

def current_timestamp() -> str:
    """
    Returns the current timestamp as a formatted string.
    Useful for logging and timestamps in reports.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_json(filepath: str, data: dict) -> None:
    """
    Save a Python dictionary as a JSON file.

    Args:
        filepath (str): Path to save the JSON file.
        data (dict): Data to be saved.
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
def load_json(filepath: str) -> dict:
    """
    Load JSON data from a file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON data.
    """
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def clamp(value: int, min_value: int, max_value: int) -> int:
    """
    Clamp an integer value between min_value and max_value.

    Args:
        value (int): Input value.
        min_value (int): Minimum allowed.
        max_value (int): Maximum allowed.

    Returns:
        int: Clamped value.
    """
    return max(min_value, min(value, max_value))

def format_percentage(value: float) -> str:
    """
    Format a float as a percentage string with 1 decimal place.

    Args:
        value (float): Value between 0 and 1.

    Returns:
        str: Percentage string, e.g., '45.3%'
    """
    return f"{value * 100:.1f}%"
