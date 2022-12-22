# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring
"""


with open('input_day_4.txt','r', encoding = 'utf8') as f:
    data = f.read().splitlines() 

count = 0

# =============================================================================
# Part_1
# for item in data:
#     
#     sectors=item.split(',')
#     
#     elf_1 = sectors[0].split('-')
#     elf_2 = sectors[1].split('-')
#     
#     elf_1_range = set([i for i in range(int(elf_1[0]), int(elf_1[1])+1)])
#     elf_2_range = set([i for i in range(int(elf_2[0]), int(elf_2[1])+1)])
#     
#     if elf_1_range.issubset(elf_2_range) or elf_2_range.issubset(elf_1_range):
#         count = count + 1
# =============================================================================
    
# Part_2

for item in data:
    
    sectors=item.split(',')
    
    elf_1 = sectors[0].split('-')
    elf_2 = sectors[1].split('-')
    
    elf_1_range = set([i for i in range(int(elf_1[0]), int(elf_1[1])+1)])
    elf_2_range = set([i for i in range(int(elf_2[0]), int(elf_2[1])+1)])
    
    overlap = set()
    overlap = (elf_1_range and elf_2_range)
    
    if not(elf_1_range.isdisjoint(elf_2_range)):
        count = count + 1


