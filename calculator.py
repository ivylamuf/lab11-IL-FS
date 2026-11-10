"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return b / a  # Raises ZeroDivisionError automatically if a == 0

def logarithm(a, b):
    return math.log(b, a)  # Raises ValueError for invalid inputs

def exponent(a, b):
    return a ** b

