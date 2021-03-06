# -*- coding: utf-8 -*-

#########################################################################
#   1.[数学] 方程求解：基于 Python，给定函数形式 y=x^2-1，给定输入 y，求解 x    #
#########################################################################

import math

#求y
def solve(y) :
    #x等于根号下y+1的绝对值
    x = math.sqrt(abs(y+1))
    x_1 = x
    x_2 = -x
    return x_1, x_2

def output(y, x_1, x_2) :
    #y+1为正，x为实数
    if y >= -1 :
        print("x_1 = %.3f" %x_1)
        print("x_2 = %.3f" %x_2)
    #y+1为负，x为虚数
    else :
        print("x_1 = %.3f*i" %x_1)
        print("x_2 = %.3f*i" %x_2)
    return 

# main
y = float(input('请输入y: '))
x_1, x_2 = solve(y)
output(y, x_1, x_2)


