import os


def test_csv_file_exists(vocab_path='ita_eng_db.csv'):
    """
    Test to check if the vocabulary CSV file exists.

    Parameters:
    - vocab_path (str): Path to the vocabulary CSV file.

    Raises:
    - AssertionError: If the vocabulary CSV file does not exist.
    """
    assert os.path.isfile(vocab_path), f"{vocab_path} does not exist"


def test_csv_file_not_empty(vocab_path='ita_eng_db.csv'):
    """
    Test to check if the vocabulary CSV file is not empty.

    Parameters:
    - vocab_path (str): Path to the vocabulary CSV file.

    Raises:
    - AssertionError: If the vocabulary CSV file is empty.
    """
    assert os.path.getsize(vocab_path) > 0, f"{vocab_path} is empty"
