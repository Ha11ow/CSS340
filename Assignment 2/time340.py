################################################################################
#
#   Author: Ben Khabazan
#   Date: 04/16/19
#   Assignment Number 2
#
################################################################################

class TimeSpan:
    minutes = 0
    hours = 0
    seconds = 0

    """
    The constructor is meant to take in 3 values, initilize them, and if 
        they are missing, set them to 0. 
    """
    def __init__(self, seconds=0, minutes=0, hours=0):
            self.setTime(seconds, minutes, hours)

    """
    Sets time to any time given (with replacement on)
    also checks to see seconds and minutes proceed 60 and adds one to a greater
        value after it, and reduces 60
    """    
    def setTime(self, seconds = 0, minutes = 0, hours = 0):
        tempHours = 0
        self.minutes = minutes
        self.seconds = seconds

        
        self.minutes += int(self.seconds / 60)
        tempHours += int(self.minutes / 60)
        self.minutes -= (int(self.minutes / 60) * 60)
        self.seconds -= (int(self.seconds / 60) * 60)
        
        if -60 <= self.seconds < 0:
            self.minutes -= 1

        if -60 <= self.minutes < 0:
            tempHours -= 1
        if type(hours) is float:
            extra = hours % 1  
            self.minutes += int(extra * 60)   
            self.hours = int(hours) 
        else:
            self.hours = hours
            
        
        self.seconds = int(self.seconds % 60)
        self.minutes = int(self.minutes % 60)
        self.hours += tempHours
    
    """
    returns the hours variable
    """
    def getHours(self):
        return self.hours

    """
    returns the minutes variable
    """
    def getMinutes(self):
        return self.minutes

    """
    returns the seconds variable
    """
    def getSeconds(self):
        return self.seconds

    """
    Creating a print method for the class, so once called it will print the 
        code bellow
    """
    def __str__(self):
        return ("Hours: " + str(self.getHours()) + ", Minutes: " 
        + str(self.getMinutes()) + ", Seconds: " + str(self.getSeconds()))
    """
    since setTime does not allow variables to be over 60s and 60m,
        I created variables outside which hold other + self and if the values 
        go above 60 i spread them, then created the instance of class
    """
    def __add__(self, other):    #make sure this is right
        
        tempHours = self.hours  + other.hours
        tempMinutes = self.minutes + other.minutes
        tempSeconds = self.seconds + other.seconds        
        
        tempMinutes += int(tempSeconds / 60)
        tempSeconds = int(tempSeconds % 60)
         
        tempHours += int(tempMinutes / 60)
        tempMinutes = int(tempMinutes % 60)
        
        tempOther = TimeSpan(tempSeconds, tempMinutes, tempHours)
        return tempOther

    """
    subtracting the values from one another, the setTime handles the 
        negative inputs by reducing from the bigger component
    """
    def __sub__(self, other):
        tempOther = TimeSpan()
        tempOther.setTime(self.seconds - other.seconds, 
        self.minutes - other.minutes, self.hours - other.hours)
        return tempOther
    
    """
    Setting each value to its negative, assuming that when doing so, the 
        seconds and minutes will be turned positive, but reducing one from the 
        hours. (hours will be negative)
    """
    def __neg__(self):
        tempOther = TimeSpan()
        tempOther.setTime(-self.seconds, -self.minutes, -self.hours)
        return tempOther

    """
    checking every value of this class, vs other class to see if they are equal 
    """
    def __eq__(self, other):
        if (self.getSeconds() == other.getSeconds() and
        self.getMinutes() == other.getMinutes() and
        self.getHours() == other.getHours()):
            return True
        else:
            return False

    """
    Checking every value to see if they are not equal to each other
    """
    def __ne__(self, other):
        if (self.getSeconds() == other.getSeconds() and
        self.getMinutes() == other.getMinutes() and
        self.getHours() == other.getHours()):
            return False
        else:
            return True

    """
    Checks to see if this class is less than the other, by checking hours first
        then minutes and then seconds
    """
    def __lt__(self, other):
        if (self.getHours() < other.getHours()):
            return True
        elif (self.getHours() > other.getHours()):
            return False
        
        if (self.getMinutes() < other.getMinutes()):
                return True
        elif (self.getMinutes() > other.getMinutes()):
            return False
            
        if (self.getSeconds() < other.getSeconds()):
                    return True
            
        return False
    """
    Just like above, checks to see if its less than, but also checks to see if
        its equal as well
    """
    def __le__(self, other):
        if (self.getHours() < other.getHours()):
            return True
        elif (self.getHours() > other.getHours()):
            return False
        
        if (self.getMinutes() < other.getMinutes()):
                return True
        elif (self.getMinutes() > other.getMinutes()):
            return False
            
        if (self.getSeconds() <= other.getSeconds()):
                    return True
            
        return False
    
    """
    Checks to see if this class is greater than the other, by checking hours
        first and then minutes then seconds
    """
    def __gt__(self, other):
        if (self.getHours() > other.getHours()):
            return True
        elif (self.getHours() < other.getHours()):
            return False
        
        if (self.getMinutes() > other.getMinutes()):
                return True
        elif (self.getMinutes() < other.getMinutes()):
            return False
            
        if (self.getSeconds() > other.getSeconds()):
                    return True
            
        return False

    """
    Just like above, its checks to see if its greater than but aslo checks to 
        see if its equal as well
    """
    def __ge__(self, other):
        if (self.getHours() > other.getHours()):
            return True
        elif (self.getHours() < other.getHours()):
            return False
        
        if (self.getMinutes() > other.getMinutes()):
            return True
        elif (self.getMinutes() < other.getMinutes()):
            return False
            
        if (self.getSeconds() >= other.getSeconds()):
            return True
        
            
        return False

    
    

        