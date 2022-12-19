from utilsAP import *
from utils import *



def apriori(itemSetList, minSupRatio, minConf,kaggle):
    if kaggle:
        itemSetList = dataReshapekaggle(itemSetList)
    else:
        itemSetList = dataReshape(itemSetList)
    # print(itemSetList)
    minSup = len(itemSetList) * minSupRatio
    # print(itemSetList)
    # print(minSup)
    C1ItemSet, F1Itemset =getItemSet(itemSetList,minSup)

    # F1Itemset = splitSetSup(C1ItemSet)


    globalFreqItemSet = []
    addItemset = addItem(F1Itemset, 2)
    i = 2
    while True:

        freqItemsetWithSup, freqItemset  = delUnderMinSup(addItemset, itemSetList, minSup)
        if (freqItemset == []):
            break

        globalFreqItemSet += freqItemset
        i=i+1



        addItemset = addItem(freqItemset, i)

    rules = associationRule(globalFreqItemSet,itemSetList,minConf)

    data = csvData(rules,itemSetList)

    return globalFreqItemSet, rules, data

