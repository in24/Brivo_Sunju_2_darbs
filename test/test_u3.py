import pytest
from src.u3 import k

def test_1(0):
    assert k(0) == 32

def test_2():
    assert k(10) == 50

def test_2(100):
    assert k(100) == 212

def test_2(-40):
    assert k(-40) == -40

def test_2(-40):
    assert k(37) == 98.6

def test_2(-40):
    assert k(-273.15) == -459.67
	