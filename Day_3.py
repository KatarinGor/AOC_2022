# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring
"""
#import csv
#import numpy as np

score_lower = [i for i in range(1,27)] 
score_upper = [i for i in range(27,57)]  

lower = list(map(chr, range(ord('a'), ord('z')+1)))
upper=(list(map(chr, range(ord('A'), ord('Z')+1))))

Score_dict = {}

for idx,item in enumerate(lower):
    Score_dict[item] = score_lower[idx]
    Score_dict[upper[idx]] = score_upper[idx]

with open('input_day_3.txt','r', encoding = 'utf8') as f:
    data = f.read().splitlines() 

sum = 0

# =============================================================================
# Part_1
# for line in data:
#     delim = int(len(line)/2)
#     line_1 = set(line[0:delim])
#     line_2 = set(line[delim:])
#     ans = list(line_1 & line_2)
#     sum = sum + Score_dict[ans[0]]
# 
# =============================================================================

for idx in range(0,len(data)-2,3):    
    line_1 = set(data[idx])
    line_2 = set(data[idx+1])
    line_3= set(data[idx+2])
    ans = list(line_1 & line_2 & line_3)
    sum = sum + Score_dict[ans[0]]


