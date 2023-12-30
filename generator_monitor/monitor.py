import re
import time


def monitor_files(file_paths, keyword, interval):
    """
    Monitors files for keyword occurrences at a specified interval.

    The function continuously checks the specified file paths for occurrences of the given keyword. If an occurrence is
    found, it logs the result using the log_result function. The checking interval between file scans can be adjusted.

    Args:
        file_paths (list): A list of file paths to monitor.
        keyword (str): The keyword to search for in the files.
        interval (int): The interval between file checks, in seconds.

    Note:
        This function runs indefinitely until interrupted or stopped manually.

    Example:
        monitor_files(["file1.txt", "file2.txt"], "important", 5)

    """
    while True:
        for file_path in file_paths:
            count = count_keyword_occurrence(file_path, keyword)
            if count > 0:
                log_result(file_path, count)
        time.sleep(interval)  # Adjust the interval between file checks here (in seconds)

def count_keyword_occurrence(file_path, keyword):
    """
    Count the occurrences of a keyword in a file.

    The function reads the contents of the specified file and counts the number of occurrences of the given keyword.
    It performs a case-sensitive, whole-word match for the keyword using regular expressions.

    Args:
        file_path (str): The path to the file to be searched.
        keyword (str): The keyword to search for.

    Returns:
        int: The number of occurrences of the keyword in the file.

    Example:
        count = count_keyword_occurrence("data.txt", "important")
        print(count)  # Output: 3

    """
    count = 0
    with open(file_path, 'r') as file:
        contents = file.read()
        count = len(re.findall(r'\b{}\b'.format(re.escape(keyword)), contents))
    return count

def log_result(file_path, count):
    """
    Log the search result to a file.

    The function appends the file path and the count of keyword occurrences to a log file named "search_results.log".
    Each log entry is written in the format "<file_path> - <count>", followed by a newline.

    Args:
        file_path (str): The path of the file for which the search result is being logged.
        count (int): The count of keyword occurrences in the file.

    Example:
        log_result("data.txt", 3)

    """
    with open("search_results.log", 'a') as file:
        file.write("{} - {}\n".format(file_path, count))
