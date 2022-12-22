# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring
"""
import re

#%%

with open('input_day_5.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()

#%%

for ind, line in enumerate(data):
    if line == '':
        num = ind
    
    
#%%

slots_str = data[num-1]
boxes = data[0:num-1]
mooves = data[num+1:]

#%%

slots = []
    
for item in slots_str:
    if item.isdigit():
        slots.append(int(item))
    
#%%
cargo={slots[i]:[] for i in range(len(slots))}

i = 0
for line in boxes[::-1]:
    for item in line[1::4]:
        if item != ' ':
            cargo[slots[i]].append(item)            
            i +=1           
        elif item ==' ':
            i +=1            
    i=0
            # print(item)
        

#%%


for idx,line in enumerate(mooves):
    mooves[idx] = re.split('move | from | to ', line)

# =============================================================================
# #%% Part_1
# 
# for item in mooves:
#     q = int(item[1])
#     key_1 = int(item[2])
#     key_2 = int(item[3])
#     
#     for t in range(1,q+1):
#         print(cargo[key_2])
#         print(cargo[key_1])
#         temp=cargo[key_1].pop(-1)
#         cargo[key_2].append(temp)
#         print(temp)
#         print(cargo[key_2])
#         print(cargo[key_1])
#         #cargo[key_2].append(temp)        
# =============================================================================

#%%
#%% Part_2

for item in mooves:
    q = int(item[1])
    key_1 = int(item[2])
    key_2 = int(item[3])
    
    l = len(cargo[key_1])
    print(cargo[key_1])
    temp = cargo[key_1][l-q:]
    print(temp)
    cargo[key_2].extend(temp)
    print(cargo[key_2])
    del cargo[key_1][l-q:]
    print(cargo[key_1])
   
    
           

#%%
ans = []
for key in cargo:
    ans.append(cargo[key][-1])     
    