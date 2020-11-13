import pytest
from src.u1 import dalijums

def tests_1():
    assert dalijums(12, 4) == 3

def tests_2():
    assert dalijums(4, -2) == -2

def tests_3():
    assert dalijums(4.5, -3) == -1.5

def tests_4():
    assert dalijums(1, 3) == 0.3333

