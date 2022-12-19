import logging
import csv
import time
from pathlib import Path
from typing import Any, List, Union
from itertools import chain, combinations
from collections import defaultdict

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running {func.__name__} ...", end='\r')
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} Done in {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def read_file(filename: Union[str, Path]) -> List[List[int]]:
    """read_file

    Args:
        filename (Union[str, Path]): The filename to read

    Returns:
        List[List[int]]: The data in the file
    """
    return [
        [int(x) for x in line.split()]
        for line in Path(filename).read_text().splitlines()
    ]
@timer
def read_csvfile(filename: Union[str, Path]) -> List[List[int]]:
    """read_file

    Args:
        filename (Union[str, Path]): The filename to read

    Returns:
        List[List[int]]: The data in the file
    """
    return [
        [x for x in line.split(',')]
        for line in Path(filename).read_text().splitlines()
    ]


@timer
def write_file(data: List[List[Any]], filename: Union[str, Path]) -> None:
    """write_file writes the data to a csv file and
    adds a header row with `relationship`, `support`, `confidence`, `lift`.

    Args:
        data (List[List[Any]]): The data to write to the file
        filename (Union[str, Path]): The filename to write to
    """
    with open(filename, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(["antecedent","consequent", "support", "confidence", "lift"])
        writer.writerows(data)


def setup_logger():
    l = logging.getLogger('l')

    log_dir: Path = Path(__file__).parent / "logs"

    # create log directory if not exists
    log_dir.mkdir(parents=True, exist_ok=True)

    # set log file name
    log_file_name = f"{time.strftime('%Y%m%d_%H%M%S')}.log"

    l.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(
        filename=log_dir / log_file_name,
        mode='w'
    )
    streamHandler = logging.StreamHandler()

    allFormatter = logging.Formatter(
        "%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s"
    )

    fileHandler.setFormatter(allFormatter)
    fileHandler.setLevel(logging.INFO)

    streamHandler.setFormatter(allFormatter)
    streamHandler.setLevel(logging.INFO)

    l.addHandler(streamHandler)
    l.addHandler(fileHandler)

    return l

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def associationRule(freqItemSet, itemSetList, minConf):
    rules = []

    for itemSet in freqItemSet:
        subsets = powerset(itemSet)

        itemSetSup = getSupport(itemSet, itemSetList)
        for s in subsets:
            confidence = float(itemSetSup / getSupport(s, itemSetList))
            if (confidence > minConf):
                rules.append([set(s), set(itemSet.difference(s)), confidence])

    return rules

def getSupport(testSet, itemSetList):
    count = 0

    for itemSet in itemSetList:
        if (set(testSet).issubset(itemSet)):
            count += 1

    return count

def getSupportRatio(testSet,itemSetList):

    return getSupport(testSet,itemSetList) / len(itemSetList)

def csvData(rules, itemSetList):
    data = []
    datatmp = []
    for i in range(len(rules)):
        # Strout = f'{rules[i][0]}tmp{rules[i][1]}tmp{getSupportRatio(rules[i][0],itemSetList)}tmp{rules[i][2]}tmp{rules[i][2]/getSupportRatio(rules[i][1],itemSetList)}'
        datatmp.append(str(rules[i][0]).replace(",",""))
        datatmp.append(str(rules[i][1]).replace(",",""))
        datatmp.append(round(getSupportRatio(rules[i][0], itemSetList), 3))
        datatmp.append(round(rules[i][2], 3))
        datatmp.append(round(rules[i][2] / getSupportRatio(rules[i][1], itemSetList), 3))
        data.append(datatmp)
        datatmp = []
    return data

def dataReshape(itemSetList):
    input_data_raw = []
    tmp = []
    transaction_id = 1
    for i in range(len(itemSetList)):
        if (itemSetList[i][0] == transaction_id):
            tmp.append(int(itemSetList[i][2]))


        else:

            transaction_id += 1
            input_data_raw.append(tmp)
            tmp = []
            tmp.append(int(itemSetList[i][2]))
    input_data_raw.append(tmp)

    return input_data_raw

def dataReshapekaggle(itemSetList):
    input_data_raw = []
    tmp = []
    transaction_id = 1
    tmp.append(str(itemSetList[0][2]))
    tmp.append(str(itemSetList[0][3]))
    for i in range(len(itemSetList)):
        if (itemSetList[i][0] == str(transaction_id)):
            tmp.append(str(itemSetList[i][1]))

        else:

            transaction_id = int(itemSetList[i][0])

            input_data_raw.append(tmp)
            tmp = []

            tmp.append(str(itemSetList[i][2]))
            tmp.append(str(itemSetList[i][3]))
            tmp.append(str(itemSetList[i][1]))
    input_data_raw.append(tmp)
    # print(input_data_raw[1])

    return input_data_raw

l = setup_logger()