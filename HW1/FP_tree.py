from utilsFP import *
from utils import *

def fpgrowth(itemSetList, minSupRatio, minConf,kaggle):
    if kaggle:
        orgitemSetList = dataReshapekaggle(itemSetList)
    else:
        orgitemSetList = dataReshape(itemSetList)

    frequency = getFrequency(orgitemSetList)

    minSup = len(orgitemSetList) * minSupRatio
    itemSetList = delundersup(orgitemSetList,minSup)
    fpTree, headerTable = createTree(itemSetList, frequency, minSup)
    if (fpTree == None):
        print('No frequent item set')
    else:
        freqItems = []
        miningTree(headerTable, minSup, set(), freqItems)
        rules = associationRule(freqItems, orgitemSetList, minConf)
        # return freqItems, rules
        data = csvData(rules,orgitemSetList)

        return freqItems, rules, data



