from math import sqrt
from nadjis import nadjis
def IzracunajP(a,b,c):
    s=nadjis(a,b,c)
    P= sqrt(s*(s-a)*(s-b)*(s-c))
    return P
