#-*- coding=utf-8 -*-

import numpy as np
p, w = np.polynomial.legendre.leggauss(100)

p2d = np.meshgrid(p, p)
w2d = np.outer(w, w)
f2d = lambda x: 0.25*(x[1]+1)*np.sqrt(0.5*(x[1]+1)+0.25*((x[1]+1)**2)*x[0]**2)
ans = f2d(p2d)*w2d
print("integrate 2d: ", ans.sum())