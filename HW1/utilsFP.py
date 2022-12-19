from collections import defaultdict

def delundersup(orgitemSetList,minSup):  # init del low sup
    itemSetListfilter = []
    itemdict = defaultdict(int)
    tmp = []
    for itemSet in orgitemSetList:
        for item in itemSet:
            itemdict[item] += 1
    itemdict = dict((item, sup) for item, sup in itemdict.items() if sup >= minSup)
    for itemSet in orgitemSetList:
        for item in itemSet:
            if(item in itemdict):
                tmp.append(item)
        if(tmp != []):
            itemSetListfilter.append(tmp)
            del tmp
            tmp = []

    return itemSetListfilter

class fptreeNode:
    def __init__(self, itemName, frequency, parentNode):
        self.itemName = itemName

        self.parent = parentNode


        self.childrenNode = {}


        self.count = frequency


        self.next = None

    def add(self, frequency):




        self.count += frequency





def createTree(itemSetList, frequency, minSup):

    rootNode = fptreeNode('Null', 1, None) # create root node
    # print(minSup)
    headerTable = defaultdict(int)
    # print(frequency)
    for idx, itemSet in enumerate(itemSetList):
        for item in itemSet:
            headerTable[item] += frequency[idx]


    headerTableCopy = headerTable.copy()
    for k in headerTableCopy.keys():  # remove items under minSup
        if headerTable[k] < minSup:
            del (headerTable[k])
    # print(headerTable)
    if (len(headerTable) == 0):
        return None, None

    headerTable = {item: [sup,None] for item, sup in headerTable.items()} # add space to store pointer



    for idx, itemSet in enumerate(itemSetList):
        # print(itemSet)
        # return
        currentNode = rootNode

        itemSet = [item for item in itemSet if item in headerTable]

        itemSet.sort(key=lambda item: headerTable[item][0], reverse=True) #sort itemset
        # print(itemSet)



        for item in itemSet:

            currentNode = updateFPTree(item, currentNode, headerTable, frequency[idx])

    return rootNode, headerTable


def updateHeaderTable(item, nextNode, headerTable):#point to next node
    if (headerTable[item][1] == None):
        headerTable[item][1] = nextNode

    else:
        currentNode = headerTable[item][1]

        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = nextNode


def updateFPTree(item, treeNode, headerTable, frequency):
    if item in treeNode.childrenNode:
        treeNode.childrenNode[item].add(frequency)
    else:# Create a new node

        newItemNode = fptreeNode(item, frequency, treeNode)
        treeNode.childrenNode[item] = newItemNode

        updateHeaderTable(item, newItemNode, headerTable)

    return treeNode.childrenNode[item]


def findAscendFPtree(node, prefixLink):
    if node.parent != None:
        prefixLink.append(node.itemName)
        findAscendFPtree(node.parent, prefixLink)


def findPrefixLink(basePat, headerTable):

    treeNode = headerTable[basePat][1]
    condPattern = []
    frequency = []
    while treeNode != None:
        prefixLink = []

        findAscendFPtree(treeNode, prefixLink)
        if len(prefixLink) > 1:

            condPattern.append(prefixLink[1:])
            frequency.append(treeNode.count)

        treeNode = treeNode.next
    return condPattern, frequency


def miningTree(headerTable, minSup, prefix, freqItemList):

    itemList = [item[0] for item in sorted(list(headerTable.items()), key=lambda p: p[1][0])]
    # print(itemList)
    for item in itemList:

        newFreqSet = prefix.copy()
        newFreqSet.add(item)
        freqItemList.append(newFreqSet)

        conditional, frequency = findPrefixLink(item, headerTable)

        conditionalTree, newHeaderTable = createTree(conditional, frequency, minSup)
        if newHeaderTable != None:
            # Mining recursively on the tree
            miningTree(newHeaderTable, minSup,
                     newFreqSet, freqItemList)




def getFrequency(itemSetList):

    frequency = [1] * len(itemSetList)

    return frequency


