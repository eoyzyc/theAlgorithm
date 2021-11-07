def merging(alist, blist):
    clist = []
    while len(alist) > 0 and len(blist) > 0:
        if alist[0] <= blist[0]:
            clist.append(alist[0])
            alist.remove(alist[0])
        else:
            clist.append(blist[0])
            blist.remove(blist[0])
    if len(alist) > 0:
        clist.extend(alist)
    else:
        clist.extend(blist)
    return clist


alist = [2,5,7]
blist = [1,3,5,8,9]                      

print(merging(alist, blist))

#clist holds your merged sorted list
#while there are still remaining items in both alist of blist
#at this point one of the lists is empty 
#put the remaining numbers in the outer list behind clist
