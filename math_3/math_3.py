import math
import euler
import quaternion as quater

def QuaternionToEuler(q:quater.Quaternion) :
    s = q.s/q.mod()
    x = q.x/q.mod()
    y = q.y/q.mod()
    z = q.z/q.mod()

    roll  = math.atan2(2*(s*x+y*z),1-2*(x*x+y*y))
    pitch = math.asin(2*(s*y-z*x))
    yaw   = math.atan2(2*(s*z+x*y),1-2*(z*z+y*y))
    e = euler.Euler(roll, pitch, yaw)

    return e

def EulerToQuaternion(e:euler.Euler) :
    def cos(x) :
        return math.cos(x)
    def sin(x) :
        return math.sin(x)

    s=cos(e.p/2)*cos(e.y/2)*cos(e.r/2) - sin(e.p/2)*sin(e.y/2)*sin(e.r/2)
    x=sin(e.p/2)*sin(e.y/2)*cos(e.r/2) + cos(e.p/2)*cos(e.y/2)*sin(e.r/2)
    y=sin(e.p/2)*cos(e.y/2)*cos(e.r/2) + cos(e.p/2)*sin(e.y/2)*sin(e.r/2)
    z=cos(e.p/2)*sin(e.y/2)*cos(e.r/2) - sin(e.p/2)*cos(e.y/2)*sin(e.r/2)
    q = quater.Quaternion(s, x, y, z)

    return q

e = QuaternionToEuler(quater.Quaternion(67, 2, 3, 4))
q = EulerToQuaternion(euler.Euler(math.pi/2, math.pi/3, math.pi/4))

print(e)
print(q)