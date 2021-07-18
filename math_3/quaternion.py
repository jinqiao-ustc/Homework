# -*- coding: utf-8 -*

class Quaternion:
    def __init__(self, s, x, y, z):
        """构造函数"""
        self.s = s
        self.x = x
        self.y = y
        self.z = z
        self.vector = [x, y, z]
        self.all = [s, x, y, z]

    def __str__(self):
        """输出操作重载"""
        op = [" ", "i ", "j ", "k"]
        q = self.all.copy()
        result = ""
        for i in range(4):
            if q[i] < -1e-8 or q[i] > 1e-8:
                if i > 0 and q[i] > 0 :
                    result = result + '+' + str(round(q[i], 4)) + op[i]
                else :
                    result = result + str(round(q[i], 4)) + op[i]
        if result == "":
            return "0"
        else:
            return result.replace(' ', '')

    def __add__(self, quater):
        """加法运算符重载"""
        q = self.all.copy()
        for i in range(4):
            q[i] += quater.all[i]
        return Quaternion(q[0], q[1], q[2], q[3])

    def __sub__(self, quater):
        """减法运算符重载"""
        q = self.all.copy()
        for i in range(4):
            q[i] -= quater.all[i]
        return Quaternion(q[0], q[1], q[2], q[3])

    def __mul__(self, quater):
        """乘法运算符重载"""
        q = self.all.copy()
        p = quater.all.copy()
        s = q[0]*p[0] - q[1]*p[1] - q[2]*p[2] - q[3]*p[3]
        x = q[0]*p[1] + q[1]*p[0] + q[2]*p[3] - q[3]*p[2]
        y = q[0]*p[2] - q[1]*p[3] + q[2]*p[0] + q[3]*p[1]
        z = q[0]*p[3] + q[1]*p[2] - q[2]*p[1] + q[3]*p[0]
        return Quaternion(s, x, y, z)

    def divide(self, quaternion):
        """右除"""
        result = self * quaternion.inverse()
        return result

    def modpow(self):
        """模的平方"""
        q = self.all.copy()
        return sum([i**2 for i in q])

    def mod(self):
        """求模"""
        return pow(self.modpow(), 1/2)

    def conj(self):
        """转置"""
        q = self.all.copy()
        for i in range(1, 4):
            q[i] = -q[i]
        return Quaternion(q[0], q[1], q[2], q[3])

    def inverse(self):
        """求逆"""
        q = self.all.copy()
        mod = self.modpow()
        for i in range(4):
            q[i] /= mod
        return Quaternion(q[0], -q[1], -q[2], -q[3])