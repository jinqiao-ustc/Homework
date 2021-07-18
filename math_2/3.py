#-*- coding=utf-8 -*-

from scipy import integrate
import math

f = lambda y, x : math.sqrt(x+y**2)

result = integrate.dblquad(f, 0, 1, lambda x: -x, lambda x: x)

print(result)