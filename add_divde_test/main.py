import pytest

def add(a,b):
    return a + b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divided by 0")
    return(a,b)