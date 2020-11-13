import pytest
from src.u5 import vienadojums

"""
Funkcija akceptē trīs argumentu - kvadrātvienādojuma 
koeficientus a,b un c.
Funcija atgriež masīvu ar saknēm vai None, ja sakņu nav.

Argumenti:
    a {int vai float} -- koeficients a (pie x^2)
    b {int vai float} -- koeficients b (pie x)
    c {int vai float} -- koeficients c
Atgriež:
    list [] -- vienādojuma saknes vai None
"""

def nav_saknes():
    assert vienadojums(2, -6, 8) == [None]

def viena_sakne():
    assert vienadojums(1, 6, 9) == [-3]




