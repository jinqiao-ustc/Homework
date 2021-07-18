#-*-coding=utf-8-*-

import math
import time
import numpy as np
from scipy import integrate

#高斯积分法解二次积分
def myfunc():
    #勒让德数列
    p, w = np.polynomial.legendre.leggauss(100)
    p2d = np.meshgrid(p, p)
    w2d = np.outer(w, w)
    #Gauss积分
    f2d = lambda x: 0.25*(x[1]+1)*np.sqrt(0.5*(x[1]+1)+0.25*((x[1]+1)**2)*x[0]**2)
    ans = f2d(p2d)*w2d
    return ans.sum()

#官方二重积分函数
def stfunc():
    f = lambda y, x : math.sqrt(x+y**2)
    result, err = integrate.dblquad(f, 0, 1, lambda x: -x, lambda x: x)
    return result


#main
#开始计时
start = time.time()
print('start test myfunc:')
for i in range(10000):
    myfunc()
time1 = time.time()
print('result:', myfunc())
print('time:', time1-start)
print('\nstart test stfunc:')
for i in range(10000):
    stfunc()
time2 = time.time()
print('result:', stfunc())
print('time:', time2-time1)
