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
import math

def vienadojums(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        atbilde = [None]
    elif d == 0:
        atbilde = [-b / (2 * a)]
    else:
        kvs_no_d = math.sqrt(d)
        x1 = (-b + kvs_no_d) / (2 * a)
        x2 = (-b - kvs_no_d) / (2 * a)
        atbilde = [x1, x2]
    return atbilde

