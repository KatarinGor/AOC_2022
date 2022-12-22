# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring
"""


#%%

with open('input_day_6.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()

#%%

data_str = data[0]

#%%
stop_iter = 0 
iter = 14

while stop_iter < len(data_str)-14:
    sub_data = data_str[iter-14:iter]
    if len(sub_data)==len(set(sub_data)):
        print(iter)
        break    
    stop_iter +=1
    iter+=1
