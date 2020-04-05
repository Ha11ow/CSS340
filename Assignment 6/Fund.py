#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5/06/2019
#     Class: Fund
#     The Fund class is a representative of the funds in an account that hold 
#     the balance for a user
#===============================================================================

class Fund:
    
    """
    The constructor for the fund only requires a name to be set, and initilizes
    the money instant as 0, it also creates a list of strings for the history,
    so every transaction can be added to it
    
    @param name: string     defaulted to ""
    """ 
    def __init__(self, name = ""):
        self.__name = name
        self.__money = 0
        self.__history = []
    
    """
    The add function will allow the account to add money into the fund
    
    @param money: int    
    """
    def add(self, money):
        self.__money += money
    
    """
    the remove function will reduce the money held in by the given amount
    
    @param monney: int
    """
    def remove(self, money):
        self.__money -= money
    
    """
    getMoney will return the money instance as an int
    """
    def getMoney(self):
        return self.__money

    """
    getName will return the name instance for the fund as a string
    """
    def getName(self):
        return self.__name
        
    def set(self, money):
        self.__money = money
        
    """
    appendHistory simply takes in an input which is supposed to be a string,
    and adds it to the history list
    
    @param: input: str
    """
    def appendHistory(self, input):
        self.__history.append(input)
        
    """
    display is basically the toString for the Fund class, however, since the 
    toString doesnt allow the same functionallity, it cannot be used
    """
    def display(self):
        retVal = ""
        for i in range(len(self.__history)):
            retVal += self.__history[i] + "\n"
        return retVal