#-*- coding=utf-8 -*-

#自定义类：欧拉角
class Euler :
    #r，p，y分别指roll，pitch，yaw
    def __init__(self, r, p, y) :
        self.r = r
        self.p = p
        self.y = y
        #all是包含三个元素的列表
        self.all = [r, p, y]

    #以表格形式输出
    def __str__(self) :
        result = ''
        e = self.all.copy()
        print('name\t value\t angle')
        op = ['roll\t', 'pitch\t', 'yaw\t']
        for i in range(3) :
            #result包含名称，弧度值和角度值
            result += op[i] + str(round(e[i], 4)) + '\t' + str(self.angle()[i]) +'\n'
        return result

    #roll的角度值
    def angleR(self) :
        pi = 3.141592653589793
        return round(self.r*180/pi, 4)

    #pitch的角度值
    def angleP(self) :
        pi = 3.141592653589793
        return round(self.p*180/pi, 4)

    #yaw的角度值
    def angleY(self) :
        pi = 3.141592653589793
        return round(self.y*180/pi, 4)

    #三者角度值列表
    def angle(self) :
        return [self.angleR(), self.angleP(), self.angleY()]