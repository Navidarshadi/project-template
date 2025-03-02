import os
# ?
#!


import sys  # 'sys' should be lowercase
from datetime import datetime
from pathlib import Path
from typing import Any, Dict  # Correct type hinting for a dictionary

import numpy as np


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


a = 10
b = 5
print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))
