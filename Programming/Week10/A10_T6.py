# Example code from the question

import copy
import time
from typing import Callable

def readValues(PValues: list[int|float]) -> None:
    # clear values list to ensure no duplicate data (reading twice)
    # open filehandle
    # read line-by-line
    #   # parse value(int) from line(str + '\n')
    #   # append value into the values list
    # close filehandle
    return None

def quickSort(PNums: list[int]) -> list[int]:
    # https://en.wikipedia.org/wiki/Bubble_sort
    return PNums

def bubbleSort(PNums: list[int]) -> list[int]:
    # https://en.wikipedia.org/wiki/Quicksort
    return PNums

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr) # param is function
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    Results: list[str] = []
    # 2. Operate
    print("Program starting.")
    readValues(Values)
    # ...
        # pass algorithm into the measureSortingTime function # import copy
        BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
        BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
        # check if 
    # 3. Cleanup
    Values.clear()
    Results.clear()
    print("Program ending.")
    return None