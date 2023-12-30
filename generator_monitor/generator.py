import random
import time
import threading

def generate_random_string():
    """
    Generate a random string.

    Returns:
        str: Randomly generated string.
    """
    if random.random() < 0.5:
        return "CDS"
    else:
        # Generate a random string of length 10
        return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", k=10))

def write_to_file(file_path):
    """
    Continuously writes random strings to a file.

    The function generates a random string using the generate_random_string function and appends it to the specified file
    repeatedly. It writes each string on a new line.

    Args:
        file_path (str): The path to the file to write the random strings to.

    Note:
        This function runs indefinitely until interrupted or stopped manually.

    Example:
        write_to_file("output.txt")

    """
    while True:
        random_string = generate_random_string()
        with open(file_path, 'a') as file:
            file.write(random_string + '\n')
        time.sleep(1)  # Adjust the interval between writes here (in seconds)
