# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring

"""
import numpy as np
#%%

with open('input_day_10.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()

#%%

data_list = []
for line in data:
    data_list.append(line.split(' '))
    
    
    
#%%Part_2

screen_line = '.'*40
screen=[]

for i in range(6):
    screen.append(screen_line)

#%%

X = 1
X_list = []
X_list.append(X)
num_cycle = 0
ans_dict={}



for line in data_list:
    if line[0]=='addx':
        num_cycle +=1
        X_list.append(X)
        num_cycle +=1
        X = X + int(line[1])
        X_list.append(X)
    else:
        num_cycle +=1
        X_list.append(X)


print('--'*10)
ans = 0
for i in range(20,260,40):
    # print(i)
    print(X_list[i-1])
    ans = ans + i*X_list[i-1]
    # print(i*X_list[i])
print(ans)

for i, item in enumerate(X_list):
    pass

#%% Part_1

# =============================================================================
# X = 1
# X_list = []
# X_list.append(X)
# num_cycle = 0
# #catch_keys = [20,60,100,140,180,220]
# #catch_keys = [i for i in range(220)]
# ans_dict={}
# 
# for line in data_list:
#     if line[0]=='addx':
#         num_cycle +=1
#         X_list.append(X)
#         num_cycle +=1
#         X = X + int(line[1])
#         X_list.append(X)
#     else:
#         num_cycle +=1
#         X_list.append(X)
# 
# 
# print('--'*10)
# ans = 0
# for i in range(20,260,40):
#     # print(i)
#     print(X_list[i-1])
#     ans = ans + i*X_list[i-1]
#     # print(i*X_list[i])
# print(ans)
# =============================================================================


