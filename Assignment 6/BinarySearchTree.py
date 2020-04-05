#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5/06/2019
#     Class: Node
#     The Node class is an inner class for the binary search tree to be able to 
#     handle the placements for the items
#===============================================================================

class Node:
    
    """
    The constructor takes in a key and a value to set up the node
    @param: key: object
    @param value: object
    """
    def __init__(self,key, value = None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None
        
    """
    will return the left child node link 
    """
    def getLeftChild(self):
        return self.__leftChild
        
    """
    will return the right child node link
    """
    def getRightChild(self):
        return self.__rightChild
        
    """
    will set the left child node link
    """
    def setLeftChild(self, link):
        self.__leftChild = link
    
    """
    will set the right child node link
    """
    def setRightChild(self, link):
        self.__rightChild = link

    """
    will get the value from the node
    """
    def getValue(self):
        return self.__value
        
    """
    will set the value for the node
    """
    def setValue(self, value):
        self.__value = value
    
    """
    will get the key from the node
    """
    def getKey(self):
        return self.__key
        
    """
    will set the key for the node
    """
    def setKey(self, key):
        self.__key = key
    
    """
    will see if there are no children set for the node (if they are null)
    """
    def isLeaf(self):
        if self.getLeftChild() == None and self.getRightChild() == None:
            return True
        return False




#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5/06/2019
#     Class: BinarySearchTree
#     A representative of the binary search tree that holds nodes as instances 
#     of the values and places them in the correct order by comparing their keys
#===============================================================================


class BinarySearchTree:
        
    """
    The constructor takes in no paramters, and only sets the root to None, 
    and the size to 0
    """
    def __init__(self):
        self.__root = None
        self.__size = 0
    
    """
    will return the size of the tree
    """
    def size(self):
        return self.__size
    
    """
    will see if the size is set to 0
    """
    def isEmpty(self):
        return self.size() == 0
        
    """
    Will return a Node if the key that is inserted matches a node in the tree
    @param  key:    the key which must be found in the tree
    """
    def get(self, key):
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                return currentNode.getValue()
            if currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else: 
                currentNode = currentNode.getRightChild()
        return None
        
    """
    Checks to see if a key exists within a tree
    @param  key:    The key that is being looked for in the tree
    """
    def contains(self, key):
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                return True
            if currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else: 
                currentNode = currentNode.getRightChild()
        return False
        
        
    """
    Overloading
    """
    def __getitem__(self, key):
        return self.get(key)
    
    """
    places the item within the tree, in the correct order after checking the 
    key to other keys within the tree.
    @param  key: that must be inserted
    @param  value: the value that must be set within the node
    """
    def put(self, key, value):
        if self.isEmpty():
            self.__root = Node(key, value)
            self.__size += 1
            return
        currentNode = self.__root
        while currentNode != None:
            if key == currentNode.getKey():
                currentNode.setValue(value)
                return
            elif key < currentNode.getKey():
                if currentNode.getLeftChild() == None:
                    temp = Node(key,value)
                    currentNode.setLeftChild(temp)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    temp = Node(key, value)
                    currentNode.setRightChild(temp)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1
    
    
    """
    Overloading
    """    
    def __setItem__(self, key, value):
        self.put(key, value)
        
    """
    This function will find the smallest node linked to the right node of the 
    intended key to be removed, removes it, and returns it.
    """
    def __getAndRemoveRightSmall(self,theNode):
        if theNode.getRightChild() == None:
            return None
        else:
            if theNode.getRightChild().getLeftChild() == None:
                tempNode = theNode.getRightChild()
                theNode.setRightChild(theNode.getRightChild().getRightChild())
                return(tempNode)
            else:
                theNode = theNode.getRightChild()

        while theNode.getLeftChild().getLeftChild() != None:
            theNode = theNode.getLeftChild()
        tempNode = theNode.getLeftChild()
        theNode.setLeftChild(theNode.getLeftChild().getRightChild())
        return tempNode
        
    """
    remove function removes a node from a node that is within the tree
    @param key: the key to find and remove the node
    """
    def remove(self, key):
        if self.contains(key) == False:
            return None
        if self.isEmpty():
            return None
        if self.__root.getKey() == key:
            self.__size -= 1
            if self.__root.getLeftChild == None:
                self.__root = self.__root.getRightChild()
            else:
                if self.__root.getLeftChild().isLeaf():
                    #set left child's right child to the right child of current Node
                    (self.__root.getLeftChild().setRightChild
                    (self.__root.getRightChild()))
                    #replace root with left child
                    self.__root = self.__root.getRightChild() 
                    
                elif self.__root.getRightChild() == None:
                    self.__root = self.__root.getLeftChild()
                
                else:                     
                    replaceNode = self.__getAndRemoveRightSmall(self.__root)
                    self.__root.setKey(replaceNode.getKey())
                    self.__root.setValue(replaceNode.getValue())
        else: 
            currentNode = self.__root
            while currentNode != None:
                if (currentNode.getLeftChild() and 
                currentNode.getLeftChild().getKey() == key):
                    foundNode = currentNode.getLeftChild()
                    if foundNode.isLeaf():
                        currentNode.setLeftChild(None)
                    elif foundNode.getLeftChild == None:
                        currentNode.setLeftChild(foundNode.getRightChild())
                    elif foundNode.getRightChild() == None:
                        currentNode.setLeftChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(foundNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    break
                elif (currentNode.getRightChild() and
                currentNode.getRightChild().getKey() == key):
                    foundNode = currentNode.getRightChild()
                    foundNode.isLeaf():
                        currentNode.setRightChild(None)
                    elif foundNode.getLeftChild() == None:
                        currentNode.setRightChild(foundNode.getRightChild())
                    elif foundNode.getRightChild == None:
                        currentNode.setRightChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(foundNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    break
                elif currentNode.getKey() > key:
                    currentNode = currentNode.getLeftChild()
                else:
                    currentNode = currentNode.getRightChild()
                
            if currentNode != None:
                self.__size -= 1

    """
    Traverses the tree in a post order to do the requried function
    @param func: function
    """    
    def postOrderTraversal(self, func):
        self.__postOrderTraversalRec(self.__root, func)
    
    """
    Traverses the tree in a post order to do the required function recursively
    @param theNode: the current node the traverse is on
    @param func: the function that is being run
    """
    def __postOrderTraversalRec(self, theNode, func):
        if theNode!= None:
            self.__postOrderTraversalRec(theNode.getLeftChild(), func)
            self.__postOrderTraversalRec(theNode.getRightChild(), func)
            func(theNode.getValue())
    
    """
    Traverses the tree inorder to do the require action
    @param func: the function that is being run
    """
    def inOrderTraversal(self, func):
        self.__inOrderTraversalRec(self.__root, func)
        
    """
    Traverses the tree inorder to do the require action recursively
    @param theNode: the current node the traverse is currently on
    @param func: the function that is being run
    """
    def __inOrderTraversalRec(self, theNode, func):
        if theNode != None:
            self.__inOrderTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getValue())
            self.__inOrderTraversalRec(theNode.getRightChild(), func)
    
    """
    Traverses the tree postorder to do the require action
    @param func: the function that is being run
    """
    def preOrderTraversal(self, func):
        self.__preOrderTraversalRec(self.__root, func)
       
    """
    Traverses the tree postorder to do the require action recursively
    @param func: the function that is being run
    """ 
    def __preOrderTraversalRec(self, theNode, func):
        if theNode!= None:
            func(theNode.getValue())
            self.__preOrderTraversalRec(theNode.getLeftChild(), func)
            self.__preOrderTraversalRec(theNode.getRightChild(), func)
                    
    """
    printValue simply takes in a value and prints it using its toString
    """
    def printValue(value):
        print(value)