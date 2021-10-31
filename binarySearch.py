def binarySearch(low, high, lst, num):
    # base case
    if low > high:
        print("Number not found")
        return False

    # recursion case
    midIndex = (low + high) // 2
    
    # if number is correct
    if num == lst[midIndex]:
        print("Number to find: " + str(num))
        print("Entire list: " + str(lst))
        print("Number found at index: " + str(midIndex))
        return True
    # if number found in upper half, chop lower half
    elif num > lst[midIndex]:
        print("\nlow is: " + str(midIndex+1))
        print("high is: " + str(high))
        return binarySearch(midIndex+1, high, lst, num)
    # if number found in lower half, chop upper half
    elif num < lst[midIndex]:
        print("\nlow is: " + str(low))
        print("high is: " + str(midIndex-1))
        return binarySearch(low, midIndex-1, lst, num)

lst = [1,4,7,11,13,15,16,18,20,35,48,78,99,110,142,175,189]
low = 0
high = len(lst) - 1
num = 8

print(binarySearch(low, high, lst, num))

