import csv
from typing import Dict, List, Tuple
import pyjokes


def create_dict(
    file_path: str, from_lan: str, to_lan: str, delimiter: str = ","
) -> Tuple[Dict[str, str], List[str]]:
    """
    Reads a CSV file with two columns and returns a dictionary
    containing the key-value pairs, and a list of the keys.

    Args:
        file_path (str): The path to the CSV file to read.
        from_lan (str): The name of the column containing the keys in the CSV file.
        to_lan (str): The name of the column containing the values in the CSV file.
        delimiter (str): The delimiter used in the CSV file. Defaults to ','.

    Returns:
        A tuple containing:
        - A dictionary with key-value pairs from the CSV file.
        - A list of keys from the CSV file.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
    """
    # Create an empty dictionary and list to hold the data
    data_dict = {}
    keys_list = []

    try:
        # Open the CSV file and create a dictionary reader
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)

            # Use a dict comprehension to create the dictionary from the CSV data
            data_dict = {rows[from_lan]: rows[to_lan] for rows in reader}
            # Get the list of keys from the dictionary
            keys_list = list(data_dict.keys())

        # Return the dictionary and list of keys as a tuple
        return data_dict, keys_list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


def tell_programming_joke():
    """
    Prints a random programming-related joke using the pyjokes library.
    """
    joke = pyjokes.get_joke(language="en", category="all")
    print(joke)
