#-*- coding=utf-8 -*-

class Euler :
    def __init__(self, r, p, y) :
        self.r = r
        self.p = p
        self.y = y
        self.all = [r, p, y]

    def __str__(self) :
        result = ''
        e = self.all.copy()
        print('name\t value\t angle')
        op = ['roll\t', 'pitch\t', 'yaw\t']
        for i in range(3) :
            result += op[i] + str(round(e[i], 4)) + '\t' + str(self.angle()[i]) +'\n'
        return result

    def angleR(self) :
        pi = 3.141592653589793
        return round(self.r*180/pi, 4)

    def angleP(self) :
        pi = 3.141592653589793
        return round(self.p*180/pi, 4)

    def angleY(self) :
        pi = 3.141592653589793
        return round(self.y*180/pi, 4)

    def angle(self) :
        return [self.angleR(), self.angleP(), self.angleY()]