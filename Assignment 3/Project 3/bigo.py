from timeit import default_timer as timer
#import numpy as np
#import random
#from matplotlib import pyplot as plt

#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 4/21/2019
#     Class: Bigo
#     Bigo is a class that tests a few find methods that searches in an array
#     for a variable and timing them
#===============================================================================


'''
find1 will traverse through the list, in order to find the value. It is a linear
    function.
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         if true => the value exists in the list,
    false => the value is not in the list
BigO = O(n^2)
'''
def find1(list, val): #with a big o of o(n)
    for index in list:
        if index == val:
            return True

    return False

'''
find2 will perform a deep copy, then sort the list, and search through with a 
    binary search to find the value.
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         if true => the value exists in the list,
    false => the value is not in the list

BigO = O(n log n)
'''
def find2(list, val): #with a big o of o(n log n) but technically more 
    temp = list[:]
    temp = sorted(temp)
    return binarySearch(temp, 0, len(temp)-1, val)


'''
binary search will perform a recursive search through the array and return with 
    true if the value is found, and false if not.
@param arr      the inputted list to be searched
@param left     the left most element searched
@param right    the right most element searched
@param val      the value that is being searched for
@return         if true => the value exists in the list,
    false => the value is not in the list

BigO = O(log n)
'''
def binarySearch(arr, left, right, val):
    if right >= left:
        mid = int( left + (right - left)/2)
        if arr[mid] == val:
            return True

        if arr[mid] > val:
            return binarySearch(arr, left, mid - 1, val)

        return binarySearch(arr, mid + 1, right, val)
    return False

'''
find3 will use the built in function from python and search for the value.
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         if true => the value exists in the list,
    false => the value is not in the list

BigO = O(n)
'''
def find3(list, val): #with a little research, the average is o(n) for lists
    if val in list:
        return True
    return False

'''
find4 perform a binary search through the presorted list.
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         if true => the value exists in the list,
    false => the value is not in the list

BigO = O(log n)
'''
def find4(list, val): #with a big o of o(log n)
    return binarySearch(list, 0, len(list) - 1, val)



#===============================================================================
#   These are helper methods for timing and creating the graph
#===============================================================================

'''
timeFind1 will time how fast the find1 method works using the inputted list and 
    val
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         time it took to perform the search
'''
def timeFind1(list, val):
    start = timer()
    find1(list, val)
    end = timer()
    print(list)    
    return (end - start)

'''
timeFind2 will time how fast the find2 method works using the inputted list and 
    val
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         time it took to perform the search
'''
def timeFind2(list, val):
    start = timer()
    find2(list, val)
    end = timer()
    print(list)
    return (end - start)

'''
timeFind3 will time how fast the find3 method works using the inputted list and 
    val
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         time it took to perform the search
'''
def timeFind3(list, val):
    start = timer()
    find3(list, val)
    end = timer()
    print(list)
    return (end - start)


'''
timeFind4 will sort the inputted list then will time how fast the find4 method 
    works using the inputted list and val
@param list     the inputted list to be searched
@param val      the value that is being searched for
@return         time it took to perform the search
'''
def timeFind4(list, val):
    tempList = sorted(list)
    start = timer()
    find4(tempList, val)
    end = timer()
    print(tempList)
    return (end - start)



#===============================================================================
#   This is the driver bellow:
#===============================================================================

if __name__ == '__main__':


    #===========================================================================
    #   Bellow is for the graphing, if you would like to test it, just uncomment
    #   I am assuming you do not have matplot, or numpy therefore removing 
    #   errors that might occure 
    #   *** NOTE: if you decide to test bellow, uncomment the imports above
    #===========================================================================
    
    """
    print("testing the timing of the functions: ")
    bigList = np.arange(-500, 501)
    random.shuffle(bigList)
    val0 = bigList[8]
    val1 = bigList[89]
    val2 = bigList[189]
    val3 = bigList[289]
    val4 = bigList[389]
    val5 = bigList[489]

    list0 = bigList[:10]
    list1 = bigList[:100]
    list2 = bigList[:200]
    list3 = bigList[:300]
    list4 = bigList[:400]
    list5 = bigList[:500]
    
    listLengths = [10,100,200,300,400,500]
    f1Times = []
    f2Times = []
    f3Times = []
    f4Times = []
    
    f1Times.append(timeFind1(list0, val0))
    f1Times.append(timeFind1(list1, val1))
    f1Times.append(timeFind1(list2, val2))
    f1Times.append(timeFind1(list3, val3))
    f1Times.append(timeFind1(list4, val4))
    f1Times.append(timeFind1(list5, val5))

    f2Times.append(timeFind2(list0, val0))    
    f2Times.append(timeFind2(list1, val1))
    f2Times.append(timeFind2(list2, val2))
    f2Times.append(timeFind2(list3, val3))
    f2Times.append(timeFind2(list4, val4))
    f2Times.append(timeFind2(list5, val5))

    f3Times.append(timeFind3(list0, val0))
    f3Times.append(timeFind3(list1, val1))
    f3Times.append(timeFind3(list2, val2))
    f3Times.append(timeFind3(list3, val3))
    f3Times.append(timeFind3(list4, val4))
    f3Times.append(timeFind3(list5, val5))

    f4Times.append(timeFind4(list0, val0))
    f4Times.append(timeFind4(list1, val1))
    f4Times.append(timeFind4(list2, val2))
    f4Times.append(timeFind4(list3, val3))
    f4Times.append(timeFind4(list4, val4))
    f4Times.append(timeFind4(list5, val5))


    plt.title('Time Vs. Elements')
    plt.ylabel('Time to find value in lists (s)')
    plt.xlabel('Number of elements in lists')
    plt.plot(listLengths, f1Times, 'bo-')

    plt.plot(listLengths, f2Times,'ro-')
    plt.plot(listLengths, f3Times, 'go-')
    plt.plot(listLengths, f4Times, 'co-')

    plt.legend(["find1", "find2", "find3", "find4"],
    loc = 'upper left', frameon = False)
    plt.show()
    plt.savefig('bigo.png')
    plt.close()
    
    """

    #===========================================================================
    #   Bellow is the driver I have created to test out every function with     
    #   different tests and inputs for errors
    #===========================================================================

    #---------------------------------------------------------------------------
    #   Find1
    #---------------------------------------------------------------------------

    print("Running tests for functions: ")

    testList1 = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    testList2 = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    
    val1 = -5
    val2 = 9
    while (len(testList1) != 0):
        print("\nUsing find1 to search testList1 for ", val1, ": ")
        if find1(testList1,val1):
            print(val1, "found at index: ", testList1.index(val1))
            testList1.remove(val1)
        else:
            print(val1, "not found in the list")

        val1 += 1
    

    print("\n\n")
   
   
    while (len(testList2) != 0):
        print("\nUsing find1 to search testList2 for ", val2, ": ")
        if find1(testList2,val2):
            print(val2, "found at index: ", testList2.index(val2))
            testList2.remove(val2)
        else:
            print(val2, "not found in the list")

        val2 -= 1


    #---------------------------------------------------------------------------
    #   Find2
    #---------------------------------------------------------------------------

    print("\n\n\n" + 
    "#=================================================================\nFind2")

    testList1 = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    testList2 = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    
    val1 = -5
    val2 = 9
    while (len(testList1) != 0):
        print("\nUsing find2 to search testList1 for ", val1, ": ")
        if find2(testList1,val1):
            print(val1, "found at index: ", testList1.index(val1))
            testList1.remove(val1)
        else:
            print(val1, "not found in the list")

        val1 += 1
    

    print("\n\n")
   
   
    while (len(testList2) != 0):
        print("\nUsing find2 to search testList2 for ", val2, ": ")
        if find2(testList2,val2):
            print(val2, "found at index: ", testList2.index(val2))
            testList2.remove(val2)
        else:
            print(val2, "not found in the list")

        val2 -= 1


    #---------------------------------------------------------------------------
    #   Find3
    #---------------------------------------------------------------------------

    print("\n\n\n" + 
    "#=================================================================\nFind3")

    testList1 = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    testList2 = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    
    val1 = -5
    val2 = 9
    while (len(testList1) != 0):
        print("\nUsing find3 to search testList1 for ", val1, ": ")
        if find3(testList1,val1):
            print(val1, "found at index: ", testList1.index(val1))
            testList1.remove(val1)
        else:
            print(val1, "not found in the list")

        val1 += 1
    

    print("\n\n")
   
   
    while (len(testList2) != 0):
        print("\nUsing find3 to search testList2 for ", val2, ": ")
        if find3(testList2,val2):
            print(val2, "found at index: ", testList2.index(val2))
            testList2.remove(val2)
        else:
            print(val2, "not found in the list")

        val2 -= 1
    
    #---------------------------------------------------------------------------
    #   Find4
    #---------------------------------------------------------------------------

    print("\n\n\n" + 
    "#=================================================================\nFind4")

    testList = [-5, 2, -3, 7, 4, 0, 9, 6, 5, -2, 3, 1, 8]
    
    testList1 = sorted(testList)
    testList2 = sorted(testList)
    
    val1 = -5
    val2 = 9
    while (len(testList1) != 0):
        print("\nUsing find4 to search testList1 for ", val1, ": ")
        if find4(testList1,val1):
            print(val1, "found at index: ", testList1.index(val1))
            testList1.remove(val1)
        else:
            print(val1, "not found in the list")

        val1 += 1
    

    print("\n\n")
   
   
    while (len(testList2) != 0):
        print("\nUsing find4 to search testList2 for ", val2, ": ")
        if find4(testList2,val2):
            print(val2, "found at index: ", testList2.index(val2))
            testList2.remove(val2)
        else:
            print(val2, "not found in the list")

        val2 -= 1