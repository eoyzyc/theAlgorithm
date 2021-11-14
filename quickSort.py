def partition(thelist, smallestIndex, largestIndex):
    pointer = smallestIndex
    pivot = thelist[largestIndex]
    for i in range(smallestIndex, largestIndex):
        if thelist[i] <= pivot:
            thelist[pointer],thelist[i] = thelist[i],thelist[pointer]
            pointer += 1
    pivot = pointer
    thelist[pivot],thelist[largestIndex] = thelist[largestIndex],thelist[pivot]
    return pivot
def quicksort(thelist, smallestIndex, largestIndex):
    if smallestIndex >= largestIndex:
        return thelist
    pivot = partition(thelist, smallestIndex, largestIndex)
    leftList = quicksort(thelist, smallestIndex, pivot - 1)
    rightList = quicksort(thelist, pivot + 1, largestIndex)
    return thelist 
thelist = [10, 7, 8, 9, 1, 5]

print(quicksort(thelist, 0, len(thelist)-1))
