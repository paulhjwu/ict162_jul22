class AddListException(Exception):
    '''Cannot have same key value'''

listA = [[1, 3], [9, 6], [4, 5] ] # [[1, 3], [4, 5], [9, 6]]
listB = [[1, 3], [4, 6], [4, 5], [2, 4] ] # [[1, 3], [2, 4], [4, 6]]
# The rule extends to compariing values, not only keys
listC = [[1, 3], [4, 6], [4, 5], [2, 4], [3, 7] ] # [[1, 3], [2, 4], [4, 6]]

listOut = []

run = 0

for aItem in listC:
    
    print(f"Run {run+1}: adding {aItem} into {listOut}")
    run += 1

    if not listOut:
        listOut.append(aItem)
    else:
        found = False # found a item in listOut that is greater than aItem
        lastIndex = len(listOut)-1
        try:
            for index, bItem in enumerate(listOut): 
                if bItem[0] == aItem[0]:
                    raise AddListException("The key should be different")
                elif bItem[0] > aItem[0]:
                    if bItem[1] < aItem[1]:
                        raise AddListException(f"Value of {aItem} must be smaller than that of {bItem} ")
                    if listOut[index-1][1]  > aItem[1]: 
                        raise AddListException(f"Value of {aItem} must be bigger than that of {listOut[index-1]} ")
                    else:
                        insertIndex = index
                        found = True
                        break
        except AddListException as e:
            print(e)
        else:
            if found:
                listOut.insert(insertIndex, aItem)
            else:
                listOut.insert(lastIndex+1,aItem)
    
    print(f"At the end of run {run} output: {listOut}")

print(listOut)

