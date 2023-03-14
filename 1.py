import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] ==  'PM':
        h = int(s[:2])
        if h < 12:
            h = h + 12
        s = str(h) + s[2:]
    else:
        if s[:2] == '12':
            h = '00'
        s = h + s[2:]          
    
    return s[:8]

if __name__ == '__main__':
    fptr = open('afzv/1/file.txt', 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()