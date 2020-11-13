import pytest
from src.u2 import laukums
def test_negativs():
    assert laukums(-1, -200) == 0
    
