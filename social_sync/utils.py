"""Utils module"""
import os


def handle_file(file_path: str):
    """
    Handle if a file exists or not and raises an exception if not.

    Parameters
    ----------
    file_path : str
        File path.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")
