from Fund import Fund


#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5/06/2019
#     Class: Account
#     Account is a class that holds 10 funds that hold the money instances, 
#     each named differently. it also has actions that are for the account 
#     such as depositing, withdrawing, and many more. 
#===============================================================================


class Account:
    
    
    """
    the Account constructor takes in a lastname, firstname, and an id
    to set up the account. then it will initilize the funds by giving them each
    a name and holding them in a list named funds
    @param  lastName: string
    @param  firstName: string
    @param  id: int
    """
    def __init__(self, lastName, firstName, id ):
        self.__id = id
        self.__funds = []

        self.__funds.append(Fund("Money Market"))
        self.__funds.append(Fund("Prime Money Market"))
        self.__funds.append(Fund("Long-Term Bond"))
        self.__funds.append(Fund("Short-Term Bond"))
        self.__funds.append(Fund("500 Index Fund"))
        self.__funds.append(Fund("Captial Value Fund"))
        self.__funds.append(Fund("Growth Equity Fund"))
        self.__funds.append(Fund("Growth Index Fund"))
        self.__funds.append(Fund("Value Fund"))
        self.__funds.append(Fund("Value Stock Index"))

        self.__firstName = firstName
        self.__lastName = lastName
        
        
    """
    The deposit method will simply check the indexing for the fund, and the
    total, and will add the money to the specified fund
    @param index: int   index for the fund
    @param total: int   total for the money to be deposited
    """
    def deposit(self, index, total):
        if index < 0 or index > 9:
            print("ERROR: Fund does not exist")
            return False
        if total > 0:
            self.__funds[index].add(total)
            self.__funds[index].appendHistory("D " + str(self.__id)
            + str(index) + " " + str(total))
            return True
            
        else:
            self.__funds[index].appendHistory("D " + str(self.__id) +
            " " + str(total) + " (Failed)")
            return False
    
    """
    transfer, basically transfers money from one account and fund, to another 
    account and fund, therefore it takes in 2 indecies, 1 total and 1 account
    @param index: int    the index for the fund
    @param total: int    the total to be transfered
    @param account: Account    the account that must be transfered to
    @param index2: int    the second index for the new account      
    """       
    def transfer(self, index, total, account, index2):
        if index < 0 or index > 9 or index2 < 0 or index2 > 9:
            print ("ERROR: Fund does not exist")
            return False
        if total > 0:
            
            #checking to see if either of the linked funds
            if index == 0 or index == 1:

                #checking if theres money in both funds
                if (self.__funds[0].getMoney() +
                self.__funds[1].getMoney() < total):
                    print("ERROR: Not enough funds to Transfer " +
                    str(total) + " from " + 
                    self.__firstName , self.__lastName ,
                    self.__funds[index].getName())
                    
                    self.__funds[index].appendHistory("T " + str(self.__id) +
                    str(index) + " " + str(total) + " " +
                    str(account.getId()) + str(index2) + " (Failed)")
                    
                    account.__funds[index2].appendHistory("T " +
                    str(self.__id) + str(index) + " " + str(total) +
                    " " +  str(account.getId()) + str(index2) + " (Failed)")
                    
                    return False
                
                #checking if theres enough money in fund
                if self.__funds[index].getMoney() >= total:
                    self.__funds[index].remove(total)
                    self.__funds[index].appendHistory("T " +
                    str(self.__id) + str(index) + " " + str(total) +
                    " " +  str(account.getId()) + str(index2))
                    
                    account.__funds[index2].add(total)
                    account.__funds[index2].appendHistory("T " +
                    str(self.__id) + str(index) + " " + str(total) +
                    " " +  str(account.getId()) + str(index2))
                    
                    return True
                else:
                    amount = (self.__funds[0].getMoney() +
                    self.__funds[1].getMoney())
                    if index == 0:
                        self.__funds[1].set(amount - total)
                        self.__funds[index].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index + 1].appendHistory("T " +
                        str(self.__id) + str(index + 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index + 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index].set(0)
                        account.__funds[index2].add(total)
                        
                        return True
                        
                    else:
                        #adding history the the first account
                        self.__funds[0].set(amount - total)
                        self.__funds[index].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        #adding history to first account
                        self.__funds[index + 1].appendHistory("T " +
                        str(self.__id) + str(index - 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        #adding history to the second account
                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        #adding history to second account
                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index - 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index].set(0) #set first account to 0
                        account.__funds[index2].add(total) #add total to second

                        return True
            
            #checking if any of the linekd accounts
            if index == 2 or index == 3:
                
                #checking if theres enough money is in both accounts
                if (self.__funds[2].getMoney() +
                self.__funds[3].getMoney() < total):
                    print("ERROR: Not enough funds to Transfer " +
                    str(total) + " from " + self.__firstName ,
                    self.__lastName , self.__funds[index].getName())
                    
                    self.__funds[index].appendHistory("T " +
                    str(self.__id) + str(index) + " " + str(total) +
                    " " +  str(account.getId()) + str(index2) + " (Failed)")
                    
                    return False

                #checking if theres enough money in initial account
                if self.__funds[index].getMoney() >= total:
                    self.__funds[index].remove(total)
                    self.__funds[index].appendHistory("T " +
                    str(self.__id) + str(index) + " " +
                    str(total) + " " +  str(account.getId()) + str(index2))

                    account.__funds[index2].appendHistory("T " + 
                    str(self.__id) + str(index) + " " + str(total) +
                    " " +  str(account.getId()) + str(index2))
                    account.__funds[index2].add(total)                    
                    return True
                    
                else:
                    amount = (self.__funds[2].getMoney() +
                    self.__funds[3].getMoney())
                    
                    #finding the correct index
                    if index == 0:
                        self.__funds[3].set(amount - total)
                        self.__funds[index].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) + 
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index + 1].appendHistory("T " +
                        str(self.__id) + str(index + 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))

                        account.__funds[index2].appendHistory("T " + 
                        str(self.__id) + str(index) + " " + 
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index + 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index].set(0)
                        account.__funds[index2].add(total)
                        
                        return True
                        
                    else:
                        self.__funds[2].set(amount - total)
                        self.__funds[index].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index + 1].appendHistory("T " +
                        str(self.__id) + str(index - 1) + " " +
                        str(total-self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))

                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index) + " " +
                        str(self.__funds[index].getMoney()) +
                        " " +  str(account.getId()) + str(index2))
                        
                        account.__funds[index2].appendHistory("T " +
                        str(self.__id) + str(index - 1) + " " +
                        str(total-self.__funds[index].getMoney()) + 
                        " " +  str(account.getId()) + str(index2))
                        
                        self.__funds[index].set(0)
                        account.__funds[index2].add(total)
                        
                        return True
            
            #checking for not enough money
            if self.__funds[index].getMoney() < total:
                #printing error
                print("ERROR: Not enough funds to Transfer " +
                str(total) + " from " + self.__firstName , self.__lastName,
                self.__funds[index].getName())
                
                #adding to the history as a failed transaction
                self.__funds[index].appendHistory("T " + str(self.__id) +
                str(index) + " " + str(total) + " " +  str(account.getId()) +
                str(index2) + " (Failed)")
                
                #adding the history as a fialed to second account
                account.__funds[index2].appendHistory("T " +
                str(self.__id) + str(index) + " " + str(total) +
                " " +  str(account.getId()) + str(index2) + " (Failed)")
                
                return False
            
            #will remove the total from the fund, and add to the other account
            self.__funds[index].remove(total)
            account.__funds[index2].add(total)
            
            #will add to the history of first account
            self.__funds[index].appendHistory("T " +
            str(self.__id) + str(index) + " " + str(total) +
            " " +  str(account.getId()) + str(index2))
            
            #will add to the second history
            account.__funds[index2].appendHistory("T " + str(self.__id) +
            str(index) + " " + str(total) + " " +  str(account.getId()) +
            str(index2))
            
            return True 

    """
    withdraw, basically withdraws money from the specidied fund
    @param index: int    the index for the fund
    @param total: int    the total to be withdrawn
    """   
    def withdraw(self, index, total):
        #checking if index is between 0 and 9
        if index < 0 or index > 9:
            print("ERROR: Fund does not exist")
            return False
            
        #checking if total is positive
        if total > 0:
            
            #if the index is linked
            if index == 0 or index == 1:
                
                #checking enough money in both accounts
                if (self.__funds[0].getMoney() +
                self.__funds[1].getMoney() < total):
                    
                    #prints the error
                    print("ERROR: Not enough funds to withdraw " +
                    str(total) + " from " + self.__firstName, self.__lastName,
                    self.__funds[index].getName())
                    
                    #adds error to history
                    self.__funds[index].appendHistory("W " +
                    str(self.__id) + str(index) + " " +
                    str(total) + " (Failed)")
                    
                    return False
                else:
                    #if total can be managed by index 
                    if self.__funds[index].getMoney() >= total:
                        self.__funds[index].remove(total)
                        self.__funds[index].appendHistory("W " +
                        str(self.__id) + str(index) + " " + str(total))
                        
                        return True
                        
                    else:
                        amount = (self.__funds[0].getMoney() +
                        self.__funds[1].getMoney())
                        
                        #if its the first index
                        if index == 0:
                            
                            #appending to history
                            self.__funds[1].set(amount - total)
                            self.__funds[index].appendHistory("W " +
                            str(self.__id) + str(index) + " " +
                            str(self.__funds[index].getMoney()))
                            
                            #appending to history
                            self.__funds[index + 1].appendHistory("W " + 
                            str(self.__id) + str(index + 1) + " " +
                            str(total-self.__funds[index].getMoney()))
                            
                            self.__funds[index].set(0)
                            return True
                        else:
                            
                            #appending to history
                            self.__funds[0].set(amount - total)
                            self.__funds[index].appendHistory("W " +
                            str(self.__id) + str(index) + " " + 
                            str(self.__funds[index].getMoney()))
                            
                            #appending to history
                            self.__funds[index - 1].appendHistory("W " +
                            str(self.__id) + str(index - 1) + " " +
                            str(total-self.__funds[index].getMoney()))
                            
                            self.__funds[index].set(0)
                            return True
            
            #checking to see if the index is linked
            if index == 2 or index == 3:
                if (self.__funds[2].getMoney() +
                self.__funds[3].getMoney() < total):
                
                    #prints errors
                    print("ERROR: Not enough funds to withdraw " +
                    str(total) + " from " + self.__firstName, self.__lastName,
                    self.__funds[index].getName())
                    
                    return False
                    
                else:
                    if self.__funds[index].getMoney() >= total:
                        self.__funds[index].remove(total)
                        self.__funds[index].appendHistory("W " +
                        str(self.__id) + str(index) + " " + str(total))
                        
                        return True
                    else:
                        amount = (self.__funds[0].getMoney() +
                        self.__funds[1].getMoney())
                        if index == 2:
                            #appending to history
                            self.__funds[3].set(amount - total)
                            self.__funds[index].appendHistory("W " +
                            str(self.__id) + str(index) + " " +
                            str(self.__funds[index].getMoney()))
                            
                            #appending to history
                            self.__funds[index + 1].appendHistory("W " +
                            str(self.__id) + str(index + 1) + " " +
                            str(total-self.__funds[index].getMoney()))
                            
                            self.__funds[index].set(0)
                            return True
                        else:
                            #appending to history
                            self.__funds[2].set(amount - total)
                            self.__funds[index].appendHistory("W " +
                            str(self.__id) + str(index) + " " +
                            str(self.__funds[index].getMoney()))
                            
                            #appending to history
                            self.__funds[index - 1].appendHistory("W " +
                            str(self.__id) + str(index - 1) + " " +
                            str(total-self.__funds[index].getMoney()))
                            
                            self.__funds[index].set(0)
                            return True
            
            if self.__funds[index].getMoney() > total:
                self.__funds[index].remove(total)
                #appending to history
                self.__funds[index].appendHistory("W " +
                str(self.__id) + str(index) + " " + str(total))
                
                return True
            else:
                #appending to history
                self.__funds[index].appendHistory("W " +
                str(self.__id) + str(index) + " " +
                str(total) + " (Failed)")
                
                #print error
                print("ERROR: Not enough funds to withdraw " +
                str(total) + " from " + self.__firstName, self.__lastName,
                self.__funds[index].getName())
                
                return False
    
    """
    will return the accounts ID
    """        
    def getId(self):
        return self.__id
    
    """
    will return the first name set for account holder
    """
    def getFirstName(self):
        return self.__firstName
       
    """
    Will return the last name set for account holder
    """ 
    def getLastName(self):
        return self.__lastName            
    
    """
    Overloading the toString method
    """
    def __str__(self):
        retVal = (self.__firstName + " " +
        self.__lastName + " Account ID: " + str(self.__id) + "\n")
        for i in range(len(self.__funds)):
           retVal += (self.__funds[i].getName() + ": $" +
           str(self.__funds[i].getMoney()) + "\n")
           
        return retVal
        
    """
    will return the history from a specific index
    """
    def getHistory(self, index):
        retVal = ("Transaction history for " + self.__firstName +
        " " +  self.__lastName + " ")
        
        retVal += (self.__funds[index].getName() +
        ": $" + str(self.__funds[index].getMoney()) +
        "\n" + self.__funds[index].display())
        
        return retVal
    
    """
    Will return the full history of all funds 
    """    
    def getFullHistory(self):
        retVal = ("Transaction history for " + self.__firstName +
        " " +  self.__lastName + " by fund.\n")
        
        for i in range(len(self.__funds)):
            if (self.__funds[i].display() != ""):
                retVal += (self.__funds[i].getName() + ": $" +
                str(self.__funds[i].getMoney()) + "\n" +
                self.__funds[i].display())
                
        return(retVal)