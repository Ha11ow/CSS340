import math
################################################################################
#
#   Author: Ben Khabazan
#   Date: 04/16/19
#   Assignment Number 2
#
################################################################################
class Circle:
    x = 0
    y = 0
    r = 1
    def __init__(self, x = 0, y = 0, r = 1):
        self.setX(x)
        self.setY(y)
        self.setRadius(r)

    def getX(self):
        return self.x
        

    def getY(self):
        return self.y


    def getR(self):
        return self.r
    

    def setX(self, x = 0):
        if x >= 0:
            self.x = x
        else: 
            self.x = 0


    def setY(self, y = 0): 
        if y >= 0:
            self.y = y
        else: 
            self.y = 0


    def setRadius(self, r = 1):
        if r >= 1:
            self.r = r
        else: 
            self.r = 1

    '''
    The equation for the area is PI * R ^2 
    '''
    def getArea(self):
        return math.pi * self.r ** 2

    """
    The equation for the perimeter is PI * R * 2
    """
    def getPerimeter(self):
        return 2 * math.pi * self.r
    
    """
    Finding the distance, then seeing if its within the radius 
    """
    def isPointWithinCircle(self,x,y):
        if (x - self.x)**2 + (y - self.y)**2 < self.r**2:
            return True
        else:
            return False