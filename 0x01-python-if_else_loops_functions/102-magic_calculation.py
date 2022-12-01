#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if b < c:
        return (a + b)
    return (a*b - c)
