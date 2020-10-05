# Date - Oct 5, 2020 By Jatin Sharma

import math
import os
import random
import re
import sys


# Complete the matchingStrings function below.
def matchingStrings(strings, queries, strings_count, queries_count):
    res = []
    for i in range(queries_count):
        c = 0
        for j in range(strings_count):
            if (strings[j] == queries[i]):
                c = c + 1
        res.append(c)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries, strings_count, queries_count)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()