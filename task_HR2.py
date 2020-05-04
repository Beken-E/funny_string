#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    s_list = []
    r_list = []
    asciidict = dict()
    alfapetTeller = range(0,500)
    for i in alfapetTeller:
        asciidict[chr(i)] = str(i)
    # print(asciidict)

    for l in asciidict: 
        for o in s:
            if l == o:
                s_list.append(asciidict[o])
            else:
                continue
        
    print(s_list)
    r_list = s_list[::-1]
    res = [[],[]]
    print(r_list)
    
    for j in range(len(s_list)):
        if j == 0:
            continue
        else:
            res[0].append(abs(int(s_list[j-1]) - int(s_list[j])))

    for k in range(len(r_list)):
        if k == 0:
            continue
        else:
            res[1].append(abs(int(r_list[k-1]) - int(s_list[k])))    
        
        # if tempor != 0:
        #     res[0].append(tempor - int(s_list[j])
        #     tempor -= tempor
        #     tempor += [int(s_list[j])
        # else:
        #     tempor += [int(s_list[j])
        #     continue


        #res[0].append(int(s_list[j]) - int(r_list[j]))

    print(res)
    if res[0] == res[1]:
        return "funny"
    else:
        return "not funny"

funnyString("2")

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         s = input()

#         result = funnyString(s)

#         fptr.write(result + '\n')

#     fptr.close()
