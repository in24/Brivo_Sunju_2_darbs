"""
B. Trijstūra laukums
Funkcija akceptē divus argumentus - trisjtūra augstumu un pamatu,
aprēķina trijstūra laukumu un atgriež to. Ja kāds no argumentiem ir mazāks vai vienāds ar 0, atgriež 0.
Formula trijstūra laukuma aprēķināšanai ir augstums*pamats/2

Argumenti:
    h {int vai float} -- trijstūra augstums
    p {int vai float} -- trijstūra pamats
Atgriež:
    int vai float -- rezultāts
"""

def laukums(h, p):
    if h > 0 and p > 0:
        rezult = h * p / 2
    else:
        rezult = 0
    return rezult
