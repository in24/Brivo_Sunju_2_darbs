import pytest
from src.u2 import laukums

def tests_1():
    assert laukums(4, 6) == 12

def tests_2():
    assert laukums(7, 9) == 31.5

def tests_3():
    assert laukums(4.32, 11.7) == 25.272

def tests_4():
    assert laukums(-4, 6) == 0
