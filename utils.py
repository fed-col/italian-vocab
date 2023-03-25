from typing import Dict, List, Tuple
import pyjokes


def create_dict(file1: str, file2: str) -> Tuple[Dict[str, str], List[str], List[str]]:
    """
    Read two text files and return a dictionary, and two lists of strings.
    :param file1: A string representing the path to a text file
    :param file2: A string representing the path to a text file
    :return: A tuple containing a dictionary where keys are strings and values are strings,
             and two lists of strings
    """
    # Open both files using the 'with' statement, which automatically closes the files when we're done with them
    with open(file1) as f1, open(file2) as f2:
        # Read all lines from the first file into a list called 'keys', and remove any newline characters
        keys = [line.strip() for line in f1.readlines()]
        # Read all lines from the second file into a list called 'values', and remove any newline characters
        values = [line.strip() for line in f2.readlines()]

    # Combine the two lists of strings into a list of tuples, and then convert that list into a dictionary
    # The resulting dictionary has keys and values that are both strings
    return dict(zip(keys, values)), keys, values


def tell_programming_joke():
    """
    Prints a random programming-related joke using the pyjokes library.
    """
    joke = pyjokes.get_joke(category="programming")
    print(joke)
