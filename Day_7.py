# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring

"""

#%%

with open('input_day_7.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()

#%

data_list = []
for line in data:
    data_list.append(line.split(' '))


#%

dir_list = []


for item in data_list:
    if (item[1] == 'cd') and (item[2] != '..'):
        dir_list.append(item[2])

dir_list_rev = dir_list[::-1]






#%
data_struct = {}
dir_sum = {}
deep = {}

for key in dir_list:
    data_struct[key] = []
    dir_sum [key] = 0
    deep[key] = 0

for idx,item in enumerate(data_list):
    
    if (item[1] == 'cd') and (item[2] != '..'):
        key = item[2]
        sublist = data_list[idx+2:]
        i=0
        while i < len(sublist):
            if (sublist[i][0] == '$'):
                break
            data_struct[key].append(sublist[i])
            i+=1           
            
#%%

for key in dir_list_rev:
    temp_sum = 0
    for i,item in enumerate(data_struct[key]):

        if item[0] == 'dir':
            k = item[1]
            #data_struct[key]= data_struct[k]
            item = data_struct[k]
        
        temp_sum = temp_sum + int(item[0])    
        data_struct[key] = [str(temp_sum)]   
    

#%%


for key,val in data_struct.items():
    for i,item in enumerate(val):
        if item[0] == 'dir':
            k = item[1]
            data_struct[key][i]= data_struct[k]

        

#%%
# =============================================================================
# from itertools import chain
# 
# data_struct_flat = {}
# for key,val in data_struct.items():
#     print(key)
#     temp_sum = 0
#     cond = True
#     temp_data = val
#     while temp_data != []:
#         
#         temp_data = list(chain.from_iterable(temp_data))
#         
#         items_for_rem = []
#         
#         for item in temp_data:
#             if type(item) == str:
#                                      
#                 if item.isdigit():
#                     temp_sum += int(item) 
#                 
#                 items_for_rem.append(item)
#                 
#         for item in items_for_rem:
#             temp_data.remove(item)    
#             
#             
#             
#     data_struct_flat[key] = temp_sum
#  
# 
# =============================================================================
        
        
        
    
        
        
    

#%%


# =============================================================================
# for key,val in data_struct.items():
#     data_struct_flat[key] = str(val).replace('[', '').replace(']', '').replace("'", '').split(', ')
#     
# =============================================================================
# =============================================================================
# #%% Подсчет сумм   
# for key,val in data_struct_flat.items():
#     for item in val:
#         #print(item)
#         if item.isdigit():
#             #print(item)
#             dir_sum[key] = dir_sum[key] + int(item)
# =============================================================================
# =============================================================================
# for key,val in data_struct_flat.items():
#     dir_sum[key] = sum(data_struct_flat[key])
# =============================================================================
             
#%% Финальная сумма     
    
final_sum = 0

for key,val in data_struct.items():
    vol = int(val[0])
    if vol < 100000:
        
        final_sum += vol

print(final_sum)
    
#%%
# =============================================================================
# key = '/'
# temp_sum = 0
# for i,item in enumerate(data_struct[key]):
# 
#     if item[0] == 'dir':
#         k = item[1]
#         data_struct[key]= data_struct[k]
#         item = data_struct[key]
#     
#     temp_sum = temp_sum + int(item[0])    
#     data_struct[key] = [str(temp_sum)]   
# 
# =============================================================================
