# -*- coding: utf-8 -*

#自定义类：四元数
class Quaternion:
    #初始化
    def __init__(self, s, x, y, z):
        self.s = s
        self.x = x
        self.y = y
        self.z = z
        self.vector = [x, y, z]
        self.all = [s, x, y, z]

    #输出操作重载
    #以1+2i+3j-5k的形式输出
    def __str__(self):
        op = [" ", "i ", "j ", "k"]
        q = self.all.copy()
        result = ""
        for i in range(4):
            if q[i] < -1e-8 or q[i] > 1e-8:
                #正值则人为添加加号
                if i > 0 and q[i] > 0 :
                    result = result + '+' + str(round(q[i], 4)) + op[i]
                else :
                    result = result + str(round(q[i], 4)) + op[i]
        if result == "":
            return "0"
        else:
            #去除result中的空格
            return result.replace(' ', '')

    #加法运算符重载
    def __add__(self, quater):
        q = self.all.copy()
        for i in range(4):
            q[i] += quater.all[i]
        return Quaternion(q[0], q[1], q[2], q[3])

    #减法运算符重载
    def __sub__(self, quater):
        q = self.all.copy()
        for i in range(4):
            q[i] -= quater.all[i]
        return Quaternion(q[0], q[1], q[2], q[3])

    #乘法运算符重载
    def __mul__(self, quater):
        q = self.all.copy()
        p = quater.all.copy()
        s = q[0]*p[0] - q[1]*p[1] - q[2]*p[2] - q[3]*p[3]
        x = q[0]*p[1] + q[1]*p[0] + q[2]*p[3] - q[3]*p[2]
        y = q[0]*p[2] - q[1]*p[3] + q[2]*p[0] + q[3]*p[1]
        z = q[0]*p[3] + q[1]*p[2] - q[2]*p[1] + q[3]*p[0]
        return Quaternion(s, x, y, z)

    #右除
    def divide(self, quaternion):
        result = self * quaternion.inverse()
        return result

    #模的平方
    def modpow(self):
        q = self.all.copy()
        return sum([i**2 for i in q])

    #求模
    def mod(self):
        return pow(self.modpow(), 1/2)

    #转置
    def conj(self):
        q = self.all.copy()
        for i in range(1, 4):
            q[i] = -q[i]
        return Quaternion(q[0], q[1], q[2], q[3])

    #求逆
    def inverse(self):
        q = self.all.copy()
        mod = self.modpow()
        for i in range(4):
            q[i] /= mod
        return Quaternion(q[0], -q[1], -q[2], -q[3])