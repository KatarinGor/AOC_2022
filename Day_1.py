# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring
"""
import csv
import numpy as np

with open('input.csv', encoding = 'utf8') as csvfile:    
    reader_object = csv.reader(csvfile, delimiter = "n")
    ans = [[]]
    count = 0
    for row in reader_object:
        if row == []:
            count += 1
            ans.append([])            
        else:
            ans[count].append(row)
            

max_sum = 0
elf_number = 0

sum_list = []
            
for idx,item in enumerate(ans):
    loc_sum = 0
    for it in item:
        loc_sum += int(it[0])
        sum_list.append(loc_sum)
    if loc_sum > max_sum:
        max_sum = loc_sum
        elf_number = idx
        
ordered_sum = sorted(sum_list, reverse = True)

answer = ordered_sum[0] + ordered_sum[1] + ordered_sum[2]

    