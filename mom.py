from math import * #pylint: disable=unused-import, unused-wildcard-import

VACPERM = 8.85418781762039e-12 # epsilon_0

# !! CLASS BULLSHIT DONT BOTHER LOL 

class Point:
    def __init__(self, *args, **kwargs): 
        self.x = 0
        self.y = 0
        self.r = 0
        self.t = 0

        # 'xy' : a tuple(2) of (x,y)
        # 'rt' : a tuple(2) of (r,t)
        # xy takes priority

        if 'xy' in kwargs:
            self.define_cartesian(kwargs['xy'][0], kwargs['xy'][1])
        elif 'rt' in kwargs:
            self.define_polar(kwargs['rt'][0], kwargs['rt'][1])


    def define_polar(self, r: float, t: float):
        self.r = r
        self.t = t
        self.__update_cartesian(r, t)

    def define_cartesian(self, x: float, y: float):
        self.x = x
        self.y = y
        self.__update_polar(x, y)

    def __update_polar(self, x: float, y: float):
        self.r = sqrt(x**2 + y**2)
        self.t = atan2(y,x)
        if (self.t < 0):
            self.t += pi/2

    def __update_cartesian(self, r: float, t: float):
        self.x = r*cos(t)
        self.y = r*sin(t)

    def __repr__(self):
        return "".join(["Point(x=", str(round(self.x, 4)), ",y=", str(round(self.y, 4)), ") or (r=", str(round(self.r, 4)), ",t=", str(round(self.t, 4)), ")"])

class PointCharge(Point):
    def __init__(self, q_init: float, perm_init: float = VACPERM):
        super().__init__()
        self.charge = q_init # in Coulomb
        self.permittivity = perm_init # in Farad/meter

    def __repr__(self):
        return "".join(["PointCharge(", str(round(self.x, 4)), ",", str(round(self.y, 4)), ") of ", str(round(self.charge, 4)), " C"])

def point_distance(A: Point, B: Point):
    return sqrt((A.x - B.x)**2 + (A.y - B.y)**2)

# !! SPICY STUFF BEGINS HERE

charges = [
    PointCharge(-0.1694e-9), 
    PointCharge(-0.1694e-9), 
    PointCharge(0.6924e-9, 4*VACPERM), 
    PointCharge(0.2688e-9, 4*VACPERM), 
    PointCharge(0.2688e-9, 4*VACPERM), 
    PointCharge(0.6924e-9, 4*VACPERM)
    ]
t = 0
for charge in charges:
    charge.define_polar(0.1, t)
    t += pi/3

# Testing whether the charges are correct (they are!)
# for charge in charges:
#     print(charge)

phi_points = [Point(xy=(0,0))]

r = 0.02
t = pi/3
while (t <= 4*pi/3):
    while (r < 0.1):
        phi_points.append(Point(rt=(r,t)))
        r += 0.02
    r = 0.02
    t += pi/3

# for point in phi_points:
#     print(point)

i=0

# perms = [3*VACPERM] + [VACPERM] * 4 + [2.5*VACPERM] * 4 + [4*VACPERM] * 8
# print(perms)

for point in phi_points:
    Phi = 0
    for charge in charges:
        Phi += -1 * (0.1 * (pi/3)) * (1/(2*pi*charge.permittivity)) * charge.charge * log(abs(point_distance(point, charge)))
#       Phi += -1 * (0.1 * (pi/3)) * (1/(2*pi*perms[i])) * charge.charge * log(abs(point_distance(point, charge)))
    print("Phi_"+str(i)+" = "+str(Phi))
    i += 1


# Mengecek untuk Phi_0
# Phi = 0
# for charge in charges:
#     print("> Distance between", phi_points[0], "and", charge, "is", point_distance(phi_points[0], charge))
#     Phi += -1 * (0.1 * (pi/3)) * (1/(2*pi*3*VACPERM)) * charge.charge * log(abs(point_distance(phi_points[0], charge)))
# print("Phi_0 = "+str(Phi))