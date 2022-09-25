#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    if len(s)>0 and len(s)<1000:
        l = list(s)
        for i in range(len(s)):
            if i==0 and l[i].isalpha():
                l[0] = l[0].upper()
            if l[i]==' ' and l[i+1].isalpha():
                l[i+1] = l[i+1].upper()
                
        return ''.join(l)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
