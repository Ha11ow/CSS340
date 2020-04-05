#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5-10/2019
#     Class: Catalan
#     The Catalan is a summation of numbers using the previous numbers before it
#     the only known case is case 0 where it is equal to 1
#===============================================================================

class Catalan():
    '''
    The constructor for the Catalan class requires one input which represents 
        the number that will be catalaned?(idk the term lol)
    The method will call the catalan method using the input
    '''
    def __init__(self, input):
        print(Catalan.catalan(input))

    '''
    The catalan method is a recursive method that takes in an input and returns
        the total catalan of it
    The method has a stopping case that if the number is bellow 0 it returns None
    else if the number is 1, it returns 1
    else it will create a loop to add up all the numbers that form before it 
        to find the catalan of it.
    '''
    def catalan (input):
        if input < 0: #this is to see if the number entered is correct
            return None
        elif input == 0: #this is the stopping case
            return 1
        else:
            n = input - 1 
            i = 0 #incrementing number
            total = 0 #final value
            while n >= 0:
                total +=  Catalan.catalan(i) * Catalan.catalan(n) 
                i+= 1
                n-= 1
            return total

if __name__ == '__main__':
    print("Catalan sequence for 10 is ")
    cat10 = Catalan(10)

    print("Catalan sequence for 4 is ")
    cat4 = Catalan(4)

    print("\n_________Testing for problems______________\n")
    
    print("Catalan sequence for -4 is ")
    cat_4 = Catalan(-4)

    print("Catalan sequence for 0 is ")
    cat0 = Catalan(0)
    print("Catalan sequence for -1 is ")
    cat_1 = Catalan(-1)
    print("Catalan sequence for 1 is ")
    cat1 = Catalan(1)
    
