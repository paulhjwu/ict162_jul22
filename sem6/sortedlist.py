listA = [[1, 3], [9, 6], [4, 5] ] # [[1, 3], [4, 5], [9, 6]]
listB = [[1, 3], [4, 6], [4, 5], [2, 4] ] # [[1, 3], [2, 4], [4, 6]]

listOut = []

run = 0

for aItem in listB:
    
    print(f"Run {run+1}: adding {aItem} into {listOut}")
    run += 1

    if not listOut:
        listOut.append(aItem)
    else:
        error = False
        found = False # found a item in listOut that is greater than aItem
        lastIndex = len(listOut)-1
        for index, bItem in enumerate(listOut): 
            if bItem[0] == aItem[0]:
                print("The key should be different")
                error = True
                break
            elif bItem[0] > aItem[0]:
                insertIndex = index
                found = True
                break
    
        if not error:
            if found:
                listOut.insert(insertIndex, aItem)
            else:
                listOut.insert(lastIndex+1,aItem)
    
    print(f"At the end of run {run} output: {listOut}")

print(listOut)

