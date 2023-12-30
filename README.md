# Generate Monitor Package

This python package provides functionality for generating pseudo-random strings and monitoring occurrences of specific keywords in files.

- **In task they told me to generate jar, but python does not support jar. Also as task java/python I believe.**

## Installation
- Create virtual enviroment

    ```
    python3 -m venv venv
    ```
- If you are using windows system run below command to activate env
    ```
    venv\Scripts\activate
    ```
- If you are using macos/linux system run below command to activate env
    ```
    source venv/bin/activate
    ```

## How to Run
- If you don't pass interval argument it will take 5 sec by default 
    ```
    python3 setup.py
    ```
- You can pass argument such give below
    ```
    python3 setup.py -i 10
    ```
    ```
    python3 setup.py --interval 10
    ```


---
- I am aware about that we can create python package by using `setup.py`, `setup.cfg` and `pyproject.toml`, due to time constraint limited to 3 hours I was not able to do that. 