`from Account import Account
from BinarySearchTree import BinarySearchTree
from queue import Queue


#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5/06/2019
#     Class: Bank
#     The Bank class is an instance of a bank in real life. The class will 
#     perform the same actions a normal bank does using its modules 
#===============================================================================


class Bank:

    
    """
    The bank constructor will initilize a BinarySearchTree, and a Queue
    it will also take in a file name and open that file, read through line by 
    line and place the strings in the queue
    @param fileName: string
    """    
    def __init__(self,fileName):
        self.__bstree = BinarySearchTree()
        self.__q = Queue()
        f = open(fileName, "r")
        for i in f:
            self.__q.put(i)
        
    """
    The execute will be where the bank executes from the queue, and finilize 
    every transaction. This means that the data that were taken earlier from 
    the file, and stored in the queue will trigger an action in the bank
    """
    def execute(self):
        #the while loop will last until the queue is empty
        while self.__q.empty() != True:
            #data is a list of strings parsed from the string in queue
            data = self.__q.get().split()
            
            
            #the following if statements will determine the type of action
            #by the first letter
            if len(data) != 0:
                #if the first letter is O
                if data[0].upper() == "O":
                    #if the value is 4 digits long and within the correct parameters 
                    if (len(data[3]) == 4 and 
                    int(data[3]) >= 1111 or int(data[3])) <= 9999: 
                        # if the account doesnt previously exist in tree
                        if self.__bstree.contains(int(data[3])) == False:
                            account = Account(data[1], data[2], int(data[3]))#new
                            self.__bstree.put(int(data[3]), account)
    
                        else:
                            print("ERROR: Account " + data[3] +
                            " is already open. Transaction refused.")
                    else:
                        print("ERROR: Account: " + data[3] +
                        " not found. Transferal refused.")
                        
                #if the first letter is D
                elif data[0].upper() == "D":
                    #if the length of the ID + fund is 5
                    if len(data[1]) == 5:
                        #if the account exists within the tree
                        if self.__bstree.contains(int(data[1][0:4])):
                            account = self.__bstree.get(int(data[1][0:4]))
                            account.deposit(int(data[1][4]), int(data[2]))#depoist
                            
                        else: 
                            print("ERROR: Account " + data[1][0:4] +
                            " not found. Transferal refused")
                    else:
                        print("ERROR: Invalid syntax for account" +
                        " number to desposit to " + data[1])
                
                #if the first letter is W
                elif data[0].upper() == "W":
                    #if the length of the ID + fund is 5
                    if len(data[1]) == 5:
                        #if the account exists within the tree
                        if self.__bstree.contains(int(data[1][0:4])):
                            account = self.__bstree.get(int(data[1][0:4]))
                            account.withdraw(int(data[1][4]), int(data[2]))#withdraw
                        
                        else: 
                            print("ERROR: Account " + data[1][0:4] + 
                            " not found. Transferal refused")
                    else:
                        print("ERROR: Invalid syntax for account" +
                        " number to withdraw from: " + data[1])
                        
                #if the first letter is T and its a transfer
                elif data[0].upper() == "T":
                    #if the first and second account and fund are 5 digits long
                    if len(data[1]) == 5 and len(data[3]) == 5:
                        #if the first and second account exists within the tree
                        if (self.__bstree.contains(int(data[1][0:4])) 
                        and self.__bstree.contains(int(data[3][0:4]))):
                            account1 = self.__bstree.get(int(data[1][0:4]))
                            account2 = self.__bstree.get(int(data[3][0:4]))
                            account1.transfer(int(data[1][4]),int(data[2]),
                            account2, int(data[3][4])) #transfer
                        else:
                            #if its the first account that doesnt exist
                            if (self.__bstree.contains(int(data[1][0:4])
                            == False)):
                                print("ERROR: Account " + data[1][0:4] + 
                                " not found. Transferal refused")
                            else:
                                print("ERROR: Account " + data[3][0:4] + 
                                " not found. Transferal refused")
                    else:
                        #if its the first account that has invalid syntax
                        if len(data[1]) != 5:
                            print("ERROR: Invalid syntax for account" +
                            " number to withdraw from: " + data[1])
                        else:
                            print("ERROR: Invalid syntax for account" +
                            " number to withdraw from: " + data[3])
                            
                #if the first letter is H then its a history
                elif data[0].upper() == "H":
                    #if the data is 4 digits (ID)
                    if len(data[1]) == 4:
                        #if the account exists within the tree
                        if self.__bstree.contains(int(data[1])):
                            account = self.__bstree.get(int(data[1]))
                            print(account.getFullHistory())
                        else:
                            print("ERROR: Account " + data[3][0:4] + 
                            " not found. Transferal refused")
                    #if the data is 5 digits (ID + FUND)
                    elif len(data[1]) == 5:
                        if self.__bstree.contains(int(data[1][0:4])):
                            account = self.__bstree.get(int(data[1][0:4]))
                            print(account.getHistory(int(data[1][4])))
                            
                        else:
                            print("ERROR: Account " + data[3][0:4] + 
                            " not found. Transferal refused")
                    else:
                        print("ERROR: Invalid syntax for account" +
                            " number to withdraw from: " + data[1])
                            
            else:
               print("ERROR: Invalid input from the file") 
            
    """
    The display will be called after the execute, and will print out the
    binary search tree in order to find all the values correctly placed
    """
    def display(self):
        print("Processing Done. Final Balances:\n ")
        self.__bstree.inOrderTraversal(BinarySearchTree.printValue)

        