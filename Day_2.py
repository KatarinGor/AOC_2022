# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring
"""
#import csv
import numpy as np

with open('input.txt','r', encoding = 'utf8') as f:
    data = f.readlines()

score = []

# =============================================================================
# Part 1
# for l in data:
#     if l == 'A X\n':
#         score.append(4)
#     elif l == 'A Y\n':
#         score.append(8)
#     elif l == 'A Z\n':
#         score.append(3)
#     elif l == 'B X\n':
#         score.append(1)
#     elif l == 'B Y\n':
#         score.append(5)
#     elif l == 'B Z\n':
#         score.append(9)
#     elif l == 'C X\n':
#         score.append(7)
#     elif l == 'C Y\n':
#         score.append(2)
#     elif l == 'C Z\n':
#         score.append(6)    
#         
# =============================================================================

# Part 2

for l in data:
    if l == 'A X\n':
        score.append(3)
    elif l == 'A Y\n':
        score.append(4)
    elif l == 'A Z\n':
        score.append(8)
    elif l == 'B X\n':
        score.append(1)
    elif l == 'B Y\n':
        score.append(5)
    elif l == 'B Z\n':
        score.append(9)
    elif l == 'C X\n':
        score.append(2)
    elif l == 'C Y\n':
        score.append(6)
    elif l == 'C Z\n':
        score.append(7)            
    
ans = np.sum(score)

# =============================================================================
# max_sum = 0
# elf_number = 0
# 
# sum_list = []
#             
# for idx,item in enumerate(ans):
#     loc_sum = 0
#     for it in item:
#         loc_sum += int(it[0])
#         sum_list.append(loc_sum)
#     if loc_sum > max_sum:
#         max_sum = loc_sum
#         elf_number = idx
#         
# ordered_sum = sorted(sum_list, reverse = True)
# 
# answer = ordered_sum[0] + ordered_sum[1] + ordered_sum[2]
# =============================================================================

    