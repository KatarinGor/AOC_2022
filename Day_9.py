# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring

Почему-то работает только для 5 элементов, потом хвост отрывается!!!!
!!!!! хвост рвется, т.к. на первом перемещении не полностью размотался!!!!!!
"""

#%%

with open('input_day_9.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()

#%%

data_list = []
for line in data:
    data_list.append(line.split(' '))

#%%

def compute_new_place(H,T):
    
    x_dist = H[0] - T[0]
    y_dist = H[1] - T[1]
    
    # в одной строке
    if H[1] == T[1]:
        if x_dist>1:
            T[0]=  T[0] + 1
        elif x_dist < -1:
            T[0] = T[0]-1
    #В одном столбце
    if H[0] == T[0]:
        if y_dist>1:
            T[1]= T[1] + 1
        if y_dist <-1:
            T[1] = T[1] -1
# Право вверх
    if (( H[0]==T[0]+2 ) and ( H[1] == T[1] + 1 )) or (( H[0] == T[0]+1 ) and ( H[1] == T[1] +2)):
        T[0] = T[0] + 1
        T[1] = T[1] +1
# Лево вверх   

    if (( H[0]==T[0]-1 ) and ( H[1] == T[1] + 2 )) or (( H[0] == T[0]-2 ) and ( H[1] == T[1] +1)):
        T[0] = T[0] - 1
        T[1] = T[1] + 1  
        
# Лево низ
    if (( H[0]==T[0] - 1 ) and ( H[1] == T[1] - 2 )) or (( H[0] == T[0] - 2 ) and ( H[1] == T[1] -1)):
        T[0] = T[0] - 1
        T[1] = T[1] - 1        
  # Право низ
    if (( H[0]==T[0]+1 ) and ( H[1] == T[1] -2 )) or (( H[0] == T[0]+2 ) and ( H[1] == T[1] -1)):
        T[0] = T[0] + 1
        T[1] = T[1] - 1
        
    # диагональные прыжки
    if H[0] == T[0]:
        if H[1] == (T[1] +2):
            T[1] = T[1]+1
        elif (H[1] == (T[1] -2)):
            T[1] = T[1] -1
    if H[1] == T[1]:
        if H[0]== T[0]-2:
            T[0]=T[0]-1
        elif H[0] == T[0] +2:
            T[0] = T[0]+1
            
    if (H[0]==T[0]+2) and (H[1]==T[1]+2):
        T[0]+=1
        T[1]+=1
    if (H[0]==T[0]-2) and (H[1]==T[1]+2):
        T[0]-=1
        T[1]+=1
    if (H[0]==T[0]-2) and (H[1]==T[1]-2):
        T[0]-=1
        T[1]-=1
    if (H[0]==T[0]+2) and (H[1]==T[1]-2):
        T[0]+=1
        T[1]-=1
        
    return T


#%%
H = [0,0]
T=[0,0]

Tail = []
for _ in range(9):
    Tail.append(T)



pos = set()
pos.add(tuple(T))

#%% 
for mov in data_list:
    print('*'*30)
    print(mov)
    print('*'*30)
    direct = mov[0]    
    steps_num = int(mov[1])
    
    if direct == 'R':
        d = [1,0]
    elif direct == 'L':
          d = [-1,0]
    elif direct == 'U':
        d = [0,1]           
    elif direct == 'D':
        d = [0,-1]
            
    
    for step in range(steps_num):
        H[0] = H[0] + d[0]
        H[1] = H[1] + d[1]
        
        temp_tail = Tail[0].copy()
        temp_head = H.copy()
        
        Tail[0] = compute_new_place(temp_head,temp_tail)
        print('--'*10)
        print('H ', H)
        
        for i in range(1,9):
            
            # print('Tail[i-1] ', Tail[i-1])
            # print('Tail[i] ',Tail[i] )
            temp_head = Tail[i-1].copy()
            temp_tail = Tail[i].copy()
            Tail[i] = compute_new_place(temp_head,temp_tail)
            # print('Tail[i] после ', Tail[i])
            
            
        #print('H ', H)
        print('Tail', Tail)
        print(Tail[-1])
        pos.add(tuple(Tail[-1]))
    
        
ans = len(pos)

print(ans)     
        


#%% Part_1
# =============================================================================
# H = [0,0]
# T=[0,0]
# pos = set()
# pos.add(tuple(T))
# 
# for mov in data_list:
#     direct = mov[0]    
#     steps_num = int(mov[1])
#     
#     if direct == 'R':
#         d = [1,0]
#     elif direct == 'L':
#          d = [-1,0]
#     elif direct == 'U':
#         d = [0,1]           
#     elif direct == 'D':
#         d = [0,-1]
#             
#     
#     for step in range(steps_num):
#         H[0] = H[0] + d[0]
#         H[1] = H[1] + d[1]
#         
#         x_dist = H[0] - T[0]
#         y_dist = H[1] - T[1]
#         
#         # в одной строке
#         if H[1] == T[1]:
#             if x_dist>1:
#                T[0]=  T[0] + 1
#             elif x_dist < -1:
#                 T[0] = T[0]-1
#         #В одном столбце
#         if H[0] == T[0]:
#             if y_dist>1:
#                 T[1]= T[1] + 1
#             if y_dist <-1:
#                T[1] = T[1] -1
#     # Право вверх
#         if (( H[0]==T[0]+2 ) and ( H[1] == T[1] + 1 )) or (( H[0] == T[0]+1 ) and ( H[1] == T[1] +2)):
#             T[0] = T[0] + 1
#             T[1] = T[1] +1
#     # Лево вверх   
# 
#         if (( H[0]==T[0]-1 ) and ( H[1] == T[1] + 2 )) or (( H[0] == T[0]-2 ) and ( H[1] == T[1] +1)):
#             T[0] = T[0] - 1
#             T[1] = T[1] + 1  
#             
#     # Лево низ
#         if (( H[0]==T[0] - 1 ) and ( H[1] == T[1] - 2 )) or (( H[0] == T[0] - 2 ) and ( H[1] == T[1] -1)):
#             T[0] = T[0] - 1
#             T[1] = T[1] - 1        
#      # Право низ
#         if (( H[0]==T[0]+1 ) and ( H[1] == T[1] -2 )) or (( H[0] == T[0]+2 ) and ( H[1] == T[1] -1)):
#             T[0] = T[0] + 1
#             T[1] = T[1] - 1      
#             
#         pos.add(tuple(T))
#         
#         print('H')
#         print(H)
#         print('T')
#         print(T)
#         print('*'*20)
#         
#         
# ans = len(pos)
# 
# print(ans)            
#         
#     
# =============================================================================               






            

        
