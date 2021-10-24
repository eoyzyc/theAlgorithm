def bubblesort(numList):
    for i in range(len(numList)):
        for j in range(len(numList)-1):
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]
                
numList = [6,4,7,4,9,2,1]
bubblesort(numList)

print(numList)



#compare consecutive pairs of numbers from left to right, if they are not in correct order, swap them 
#after 1 iteration, the largest number will be at the back of the array 
#repeat the first few steps with the the remaining N-1 numbers 
#after N-1 iterations, the entire array will be sorted 
