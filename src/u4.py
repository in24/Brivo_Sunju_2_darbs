def f_nosaukums(f):
    c = (f - 32) * 5/9   
    if c < -273.15:
        c = -273.15
    return c
