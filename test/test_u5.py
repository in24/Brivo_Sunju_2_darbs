import pytest
from src.u5 import vienadojums

def nav_saknes():
    assert vienadojums(2, -6, 8) == [None]

def viena_sakne():
    assert vienadojums(1, 6, 9) == [-3]

def viena_sakne():
    assert vienadojums(1,-4,3) == [3, 1]





