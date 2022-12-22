# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring

"""

#%%

import numpy as np

#%%

with open('input_day_8.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()
        
        
#%%
forest_list = []

for line in data:
    temp = []
    for i in line:
        temp.append(int(i)) 
    forest_list.append(temp)        


#%%
forest = np.array(forest_list)

#%% Part_1
# =============================================================================
# st,col = forest.shape
# count = 0
# 
# for i in range(1,st-1):
#     for j in range(1,col-1):
#         tree = forest[i,j]
#         line_v_u = max(forest[0:i,j])
#         line_v_d = max(forest[i+1:,j])
#         
#         line_h_l = max(forest[i,0:j])
#         line_h_r = max(forest[i,j+1:])
#         
#         if (tree > line_v_u) or (tree > line_v_d) or (tree > line_h_l) or (tree > line_h_r):
#             count += 1
#             
# ans = count + 2*st + 2*(col - 2)
#         
# print(ans)     
# =============================================================================
        
        
 #%% Part_2
st,col = forest.shape

count = np.zeros([st, col])

for i in range(1,st-1):
    for j in range(1,col-1):
        tree = forest[i,j]
        line_v_u = forest[:i,j]
        line_v_u_r = line_v_u[::-1]
        
        line_v_d = forest[i+1:,j]
         
        line_h_l = forest[i,0:j]
        line_h_l_r = line_h_l[::-1]
                
        line_h_r = forest[i,j+1:]
        
        mask_u = (tree > line_v_u_r)
        mask_d = (tree > line_v_d)
        mask_l = (tree > line_h_l_r)
        mask_r = (tree > line_h_r)
        
        mask_list = [mask_u, mask_d, mask_l, mask_r]
        viz_list = [1,1,1,1]
                        
        for idx,mask in enumerate(mask_list):
            for item in mask:
                if item:
                    viz_list[idx] +=1
                else:
                    break
        
        if viz_list[0]>=i:
            viz_list[0] = viz_list[0]-1
            
        if viz_list[1]>=st-i:
            viz_list[1] = viz_list[1]-1
            
        if viz_list[2]>=j:
            viz_list[2] = viz_list[2]-1
            
        if viz_list[3]>=col-j:
            viz_list[3] = viz_list[3]-1       
        
       
        
        if i == 1:
            viz_list[0]=1
        if i == st-2:
           viz_list[1]=1 
           
        if j==1:
            viz_list[2]=1
        if j == col-2:
           viz_list[3]=1
           
        # Если просматривается насквозь
        

            
        
            
            
            
        

        print(i,j) 
        print(tree)
        print(viz_list)                                

        
        viz_count = viz_list[0]*viz_list[1]*viz_list[2]*viz_list[3]
        
        count[i,j] = viz_count
            
        
       

         
        
             
ans = np.max(count)
         
print(ans)            
        