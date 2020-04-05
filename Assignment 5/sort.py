#-------------------------------------------------------------------------------
#     Author: Ben Khabazan
#     Date: 5/19/2019
#     Module: sort
#     the sort mod
#===============================================================================


'''
This is the bubble sort where it will compare elements two by two and go to the 
end, this will repeat until the second to the last element is looped through
the first loop
'''
def bubbleSort(input):
    for i in range(len(input)): 
        for j in range(0, (len(input))-i-1): 
            if input[j] > input[j+1] : 
                input[j], input[j+1] = input[j+1], input[j]

'''
The insertion sort will check the elements and sort them in the correct order 
they belong from the previously checked elements
'''
def insertionSort(input): 
    for i in range(1, len(input)): 
        temp = input[i]
        j = i-1 #elements before
        while j >= 0 and temp < input[j] : 
            input[j + 1] = input[j] 
            j -= 1 #decrement to the correct spot
        input[j + 1] = temp
   
'''
This is used for the quick sort algorithm
'''
def insertionSort1(input, first, last): 
    for i in range(first+1, last+1): 
        temp = input[i]
        j = i-1 #decrementing
        while j >= first and temp < input[j] : 
            input[j + 1] = input[j] 
            j -= 1
        input[j + 1] = temp     
        
'''
The merge sort will be recursively calling itself each time with smaller size
list to reach size of 1, then will start comparing each group and putting them
back together
'''
def mergeSort(input):
    if len(input) < 2:
        return input
    m = len(input)//2
    l = input[:m]
    r = input[m:]
    
    mergeSort(l)
    mergeSort(r)
    
    i = j = k = 0
    
    while i < len(l) and j < len(r):
        if l[i] < r[j]: #fillout right 
            input[k] = l[i]
            i+=1
        else:#fillout left
            input[k] = r[j]
            j+=1
        k+=1
        
    while i < len(l):#leftover for left side
        input[k] = l[i]
        i+=1
        k+=1
        
    while j < len(r): #leftover for right side
        input[k] = r[j]
        j+=1
        k+=1
    
'''
The iterative merge sort will use loops to index down to the smallest possible
size of list, and compare the elements and groups and sort them as they go
'''
def iterativeMergeSort(input): 
    groups = 1
    while groups < len(input) - 1:
        left = 0
        while left < len(input)-1:
            right = ((2* groups + left - 1, len(input) - 
            1)[2 * groups + left - 1> len(input)-1])

            mid = left + groups - 1
            if (mid > right): #ending point
                mid = right 
            l1 = mid - left + 1
            l2 = right - mid
            leftInput = [0] * l1 
            rightInput = [0] * l2 
            for i in range(0, l1 ): 
                leftInput[i] = input[left + i] 
                
            for i in range(0, l2): 
                rightInput[i] = input[mid + i + 1] 
    
            i, j, k = 0, 0, left
            while i < (mid - left + 1) and j < (right - mid):
                if leftInput[i] > rightInput[j]:
                    input[k] = rightInput[j]
                    j+=1
                else:
                    input[k] = leftInput[i]
                    i+=1
                k+=1
                
            while i < (mid - left + 1): #remaining copies from left side
                input[k] = leftInput[i]
                i+=1
                k+=1
                
            while j < (right - mid): #remaining from right side
                input[k] = rightInput[j]
                j+=1
                k+=1
                
            left = left + groups*2
        groups = 2 * groups
        
'''
The quick sort will call the insertion sort if the list is smaller than size 5
else it would loop at the first, middle, and last index and sort them, 
then it would find the pivot and start working its way to sort the list 
from the top down by swapping elements to the correct spot when recursively 
calling itself with smaller sizes
'''
def quickSorter(input,first,last):
    if last - first < 5: 
        insertionSort1(input,first,last)
        return
    mid = (first + last) //2
    if input[first] > input[last]:
        input[first],input[last] = input[last], input[first]
    if input[first] > input[mid]:
        input[first],input[mid] = input[mid],input[first]
    if input[mid] > input[last]:
        input[mid], input[last] = input[last],input[mid]
    pivot = input[mid]
    input[last-1], input[mid] = input[mid],input[last-1]
    left = first + 1
    right = last - 2
    done = False
    while not done:
        while input[left] < pivot:
            left += 1
        while input[right] > pivot:
            right -= 1
        if right > left:
            input[left], input[right] = input[right],input[left]
            left += 1
            right -= 1
        else:
            done = True
    input[left] , input[last-1] = input[last-1], input[left]
    quickSorter(input, first, left-1)
    quickSorter(input, left+1, last)

'''
this method starts the quick sort above
'''
def quickSort(input):
    quickSorter(input,0, len(input)-1)

'''
This is the shell sort, where it will check items in the array as it goes from
the size of the list divided by two all the way to 1, this will allow it to 
sort them items much faster than insertion sort
'''        
def shellSort(input): 
    n = len(input) 
    gap = n//2
    while gap > 0: 

        for i in range(gap,n): 
            temp = input[i] 
            j = i 
            while  j >= gap and input[j-gap] >temp: 
                input[j] = input[j-gap] 
                j -= gap 
            input[j] = temp 
        gap//= 2
            

    

        