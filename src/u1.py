"""
Funkcija akceptē divus argumentus - skaiļus a un b,
aprēķina to dalījumu un atgriež to. Ja skaiļus dalīt nedrīkst,
atgriež 0.

Argumenti:
    a {int vai float} -- pirmais skaitlis
    b {int vai float} -- otrais skaitlis
Atgriež:
    int vai float -- rezultāts
"""

def dalijums(a,b):
    if b == 0:
        dal = 0
    else:
        dal = a / b
    return dal

