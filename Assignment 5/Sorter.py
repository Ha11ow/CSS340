import sort
from timeit import default_timer as timer
from matplotlib import pyplot as plt
import random
class Sorter:
    
    '''
    The Sorter constructor will intake 2 parameters, one being the sorting 
    algorithm used, and the other the length of the list size
    then the constructor will call the ranGenerator to create a random list
    of that size, and then sort it using the timeIt fucntion which will time it,
    as well as printing the sorted lists. 
    '''
    def __init__(self, sortName, length):
        tempList = Sorter.ranGenerator(length)
        time = Sorter.timeIt(sortName, tempList)
        print(time)

    '''
    the ranGenerator will fill intake an int, and create a list, and fill it to 
    the int provided with random numbers between 0 and that int
    '''
    def ranGenerator(length):
        if(type(length) == int):
            tempList = []
            for i in range(length):
               temp = random.randint(1,length)
               tempList.append(temp)
            return tempList

    '''
    The timeIt method will find the correct sorting algorithm based on the 
    string inputted, and will time the function as well as the list 
    once it is sorted.
    '''
    def timeIt(sortName, input):
        time = 0
        if(type(sortName) == str):
            if(sortName.lower() == "bubblesort"):
                start = timer()
                sort.bubbleSort(input)
                end = timer()
                print("bubble sort: \n",input)
                time = (end - start)
                
            if(sortName.lower() == "insertionsort"):
                start = timer()
                sort.insertionSort(input)
                end = timer()
                print("insertion sort: \n",input)
                time = (end - start)
                
            if(sortName.lower() == "mergesort"):
                print("merge sort2: \n",input)
                start = timer()
                sort.mergeSort(input)
                end = timer()
                print("merge sort: \n",input)
                time = (end - start)
                
            if(sortName.lower() == "iterativemergesort"):
                start = timer()
                sort.iterativeMergeSort(input)
                end = timer()
                print("iterative merge sort: \n",input)
                time = (end - start)
            
            if(sortName.lower() == "quicksort"):
                start = timer()
                sort.quickSort(input)
                end = timer()
                print("quick sort: \n",input)
                time = (end - start)
                
            if(sortName.lower() == "shellsort"):
                start = timer()
                sort.shellSort(input)
                end = timer()
                print("shell sort: \n",input)
                time = (end - start)
                
        return time
        
    '''
    the graphIt function will automatically create lists between sizes 0 and 
    2900 every 400 indices and will time how long each sort will take to sort 
    them and graph the output. 
    '''
    def graphIt():

        BStime = [0]
        IStime = [0]
        MStime = [0]
        IMStime = [0]
        QStime = [0]
        SStime = [0]
        elements = [0]
        
        for i in range (0, 2900, 400):
            temp = Sorter.ranGenerator(i)
            temp2 = temp[:]
            temp3 = temp[:]
            temp4 = temp[:]
            temp5 = temp[:]
            temp6 = temp[:]
            BStime.append(Sorter.timeIt("bubblesort", temp))
            print("\n\n", temp2, "\n\n")
            IStime.append(Sorter.timeIt("insertionsort", temp2))
            MStime.append(Sorter.timeIt("mergesort",temp3))
            IMStime.append(Sorter.timeIt("iterativemergesort",temp4))
            QStime.append(Sorter.timeIt("quicksort",temp5))
            SStime.append(Sorter.timeIt("shellsort",temp6))
            elements.append(i)
        
        plt.cla()
        plt.title('Time Vs. Elements')
        plt.ylabel('Time to sort lists (s)')
        plt.xlabel('number of elements in lists')
        plt.plot(elements, BStime, 'ro-')
        plt.plot(elements, IStime, 'co-')
        plt.plot(elements, MStime, 'mo-')
        plt.plot(elements, IMStime, 'go-')
        plt.plot(elements, QStime, 'yo-')
        plt.plot(elements, SStime, 'bo-')
        
        plt.legend(["Bubble Sort", "Insertion Sort", "Merge Sort",
        "Iterative Merge Sort", "Quick Sort", "Shell Sort"],
            loc = 'upper left', frameon = False)
        plt.show()
        
        
        
'''
this driver automatically shows the graph, which explains every list as well
'''     
if __name__ == "__main__":
    Sorter.graphIt()