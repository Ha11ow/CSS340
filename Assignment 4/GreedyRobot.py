#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5-10/2019
#     Class: GreedyRobot
#     The GreedyRobot class shows the possible minimal ways a robot can take to
#     a treasure. 
#===============================================================================

class GreedyRobot():

    '''
    The constructor inputs 4 different integers where they are set to 0 if 
        left empty, that represent the coordinations to a robot and a treasure
    The method initilizes the robot and treasure, and sends them to another 
        method called count where it finds and prints the possible ways to 
        the treasure
    '''
    def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        robot = [x1,y1]
        treasure = [x2,y2]
        if robot == treasure: 
            print("you are already on the treasure")
        else:
            print("number of paths:", GreedyRobot.count(robot, treasure, []))
    
    
    '''
    Count method will recursively call itself to find the minial possible ways 
        to a treasure
    If the robot and treasure lay on the same coordination, it will return 1, 
        meaning it has found 1 way to get there (you are on it)
    else if the directions suggest to go North or South, you do so by changing 
        the Y coordination and the East and West by changing the X coordination
    In this assignment I count being on the treasure as one path, for the path 
        is being on it.
    '''
    def count(robot, treasure, path):
        if robot[0] == treasure[0] and robot[1] == treasure[1]:
            GreedyRobot.printList(path)# of they lay on one another print path
            return 1
        
        xDirection = treasure[0] - robot[0] #finds the difference for x
        yDirection = treasure[1] - robot[1] #finds the difference for y
        retVal = 0 #number of paths possible
        
        if yDirection > 0: #if it has to go up one step
            holder = path[:]
            holder.append("N")
            retVal += GreedyRobot.count( [robot[0], robot[1] + 1], treasure, holder)
            
        
        if xDirection > 0: #if it has to go right one step
            holder = path[:]
            holder.append("E")
            retVal += GreedyRobot.count( [robot[0] + 1, robot[1]], treasure, holder)
        
        
        if yDirection < 0: #if it has to go down one step
            holder = path[:]
            holder.append("S")
            retVal += GreedyRobot.count( [robot[0], robot[1] - 1], treasure, holder)
    
        if xDirection < 0: #if it has to go left one step
            holder = path[:]
            holder.append("W")
            retVal += GreedyRobot.count( [robot[0] - 1, robot[1]], treasure, holder)
        return retVal #finally return the number of possible paths
    

    '''
    A helper method that helps print the list just as it was shown in the example
    '''
    def printList(list): 
        retVal = ""
        for i in list:
            retVal += i
        print(retVal)
            

if __name__ == "__main__":
    test = GreedyRobot(1,2,3,5)
    print("\n testing for errors and boundaries")
    print("\n testing (1,1) and (1,1)")
    test2 = GreedyRobot(1,1,1,1)
    print("\n testing no inputs")
    test3 = GreedyRobot()
    print("\n testing (2,1) and (2,4)")
    test4 = GreedyRobot(2,1,2,4)
    print("\n testing (1,2) and (5,2)")
    test5 = GreedyRobot(1,2,5,2)
    print("\n testing (-1,1) and (1,-1)")
    test6 = GreedyRobot(-1,1,1,-1)

    x1, y1, x2, y2 = [int(x) for x in input("Enter four values: ").split()] 
    test7 = GreedyRobot(x1,y1,x2,y2)
    