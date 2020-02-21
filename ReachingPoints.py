#!/bin/python

import math
import os
import random
import re
import sys


from fractions import gcd
#
# Complete the 'canReach' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

def canReach(x1, y1, x2, y2):
    # Write your code here
    if x1 > x2 or y1 > y2:
        return "No"
    if (y1==y2):
        if gcd(x2,y2) == gcd(x1,y1):
            return "Yes"
    else:
        if gcd(x2,y2) == gcd(x1,y1) == gcd(y1,y2):
            return "Yes"
    return "No"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1 = int(raw_input().strip())

    y1 = int(raw_input().strip())

    x2 = int(raw_input().strip())

    y2 = int(raw_input().strip())

    result = canReach(x1, y1, x2, y2)

    fptr.write(result + '\n')

    fptr.close()
