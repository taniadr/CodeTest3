#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'getScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getScore(s):
    # Write your code here  
    n=len(s)
    m=[]

    for i in range(n):
        vet=[]
        for j in range(n):
            vet.append(0)
        m.append(vet)

    for i in range(n):
        for j in range(n):
            if i+j == n:
                break
            if i==0:
                m[i][j]=1
            else:
                if i==1:
                    m[i][j]=1
                    if s[j] == s[j+i]:
                        m[i][j]=2
                else:
                    tmp=0
                    if s[j] == s[j+i] :
                        tmp=2
                    m[i][j] = max(m[i-2][j+1]+tmp, m[i-1][j],m[i-1][j+1])
    resp = 0
    for i in range(0, n-1):
        resp = max(resp, m[i][0]*m[n-i-2][i+1])
    
    return resp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = getScore(s)

    fptr.write(str(result) + '\n')

    fptr.close()
