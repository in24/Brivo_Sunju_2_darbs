"""Funkcija akceptē vienu argumentu - temperatūru Fārenheita grādos,
un atgriež temperatūru Celsija grādos. Zemākā temperatūra
Celsija grādos var būt −273.15, tādēļ, ja aprēķinātā temperatūra ir zemāka, atgriež −273.15.

Argumenti:
    t {int vai float} -- temperatūra Fārenheita grādos
Atgriež:
    int vai float -- temperatūra Celsija grādos"""
import pytest
from src.u4 celsijs

def test_poz():
    assert celsijs(59)==15

def test_poz():
    assert celsijs(38.3)==3.5

def test_neg():
    assert celsijs(-500)==-273.15
