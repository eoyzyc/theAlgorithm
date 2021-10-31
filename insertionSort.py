def insertionSort(lst):
    for i in range(1,len(lst)):
        currItem = lst[i]
        j = i-1
        
        while j >= 0 and currItem < lst[j]:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = currItem
lst = [1,6,5,8,2,9,11]
insertionSort(lst)
if len(lst) % 2 == 0:
    num1 = lst[len(lst)//2-1]
    num2 = lst[len(lst)//2]
    anwswer = (num1 + num2) / 2
else:
    answer = lst[len(lst)//2]
print(answer)



dic = {"T":76, "J":89, "H":19, "Jo":49, "To":24}
lst = []
for key,value in dic.items():
    lst.append(value)
insertionSort(lst)
if len (Ist) % 2 == 0:
    num1 = lst[len(lst)//2-1]
    num2 = lst[len(Ist)//2]
    anwswer = (num1 + num2) / 2
else:
    answer = lst[len(lst)//2]
print(answer)
