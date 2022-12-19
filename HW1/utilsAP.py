def getItemSet(itemSetList,minSup):
    C1 = []
    itemlist = []
    tmp = []
    itemSetListOut = []

    for transaction in itemSetList:
        for item in transaction:
            if not item in itemlist:
                itemlist.append(item)
    # C1.sort()
    # print(len(itemlist))
    for i in range(len(itemlist)):
        s = set()
        s.add(itemlist[i])
        # print(getSupport(s,itemSetList))

        if(getSupport(s,itemSetList) > minSup):
            tmp.append(s)
            itemSetListOut.append(s)
            tmp.append(getSupport(s,itemSetList))
            C1.append(tmp)
            tmp = []

    return C1,itemSetListOut

def delUnderMinSup(itemSetList,orgitemSetList,minSup):



    itemSetListWithSup = []
    itemSetListOut = []



    for item in itemSetList:
        # print("item",item)
        if(getSupport(item,orgitemSetList) > minSup):
            itemSetListWithSup.append(item)
            itemSetListOut.append(item)
            itemSetListWithSup.append(getSupport(item,orgitemSetList))



    return itemSetListWithSup, itemSetListOut



def addItem(itemSet, length):
    tmp = []


    [tmp.append(i.union(j)) for i in itemSet for j in itemSet if len(i.union(j)) == length]
    # for i in itemSet:
    #     for j in itemSet:
    #         a = i.union(j)
    #
    #         if(len(i.union(j)) == length):
    #             tmp.append(i.union(j))
    res = []
    [res.append(x) for x in tmp if x not in res]
    return res


def getSupport(testSet, itemSetList):
    count = 0
    for itemSet in itemSetList:
        if (set(testSet).issubset(itemSet)):
            count += 1
    return count
