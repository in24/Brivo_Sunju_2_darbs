import pytest
from src.u3 import kelvins

def test_1():
    assert kelvins(-273.15) == 0

def test_2():
    assert kelvins(-50) == 223.15

def test_3():
    assert kelvins(-10) == 263.15

def test_4():
    assert kelvins(0) == 273.15

def test_5():
    assert kelvins(21) == 294.15

def test_6():
    assert kelvins(37) == 310.15

def test_7():
    assert kelvins(100) == 373.15

def test_8():
    assert kelvins(1000) == 1273.15


"""
-273.15 °C	0 K	absolute zero temperature
-50 °C	223.15 K	 
-40 °C	233.15 K	 
-30 °C	243.15 K	 
-20 °C	253.15 K	 
-10 °C	263.15 K	 
0 °C	273.15 K	freezing/melting point of water
10 °C	283.15 K	 
20 °C	293.15 K	 
21 °C	294.15 K	room temperature
30 °C	303.15 K	 
37 °C	310.15 K	average body temperature
40 °C	313.15 K	 
50 °C	323.15 K	 
60 °C	333.15 K	 
70 °C	343.15 K	 
80 °C	353.15 K	 
90 °C	363.15 K	 
100 °C	373.15 K	boiling point of water
200 °C	473.15 K	 
300 °C	573.15 K	 
400 °C	673.15 K	 
500 °C	773.15 K	 
600 °C	873.15 K	 
700 °C	973.15 K	 
800 °C	1073.15 K	 
900 °C	1173.15 K	 
1000 °C	1273.15 K	
"""