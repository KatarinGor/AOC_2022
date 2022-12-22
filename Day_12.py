# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:30:43 2022

@author: Catring

Понятия не имею, как это решать. Удалось только распарсить файл. 
Нужно или строить граф, или дерево решений. Ноя не знаю, как

"""
import numpy as np
#%%

with open('input_day_12.txt','r', encoding = 'utf8') as f:  
        data = f.read().splitlines()

#%%
    
h_map = np.zeros([len(data), len(data[0])])
#%%

lower = list(map(chr, range(ord('a'), ord('z')+1)))

trans = {}
for i,let in enumerate(lower):
    trans[let] = i
    
#%%
for i_line, line in enumerate(data):
    for i_letter, letter in enumerate(line):
        if letter == 'S':
            h_map[i_line,i_letter] = 1000
            start = [i_line,i_letter]
        elif letter == 'E':
            h_map[i_line,i_letter] = 2000
            stop = [i_line,i_letter]
        else:            
            h_map[i_line,i_letter] = trans[letter]
        
#%%        
# =============================================================================
# nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
# distances = {
#     'B': {'A': 5, 'D': 1, 'G': 2},
#     'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
#     'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
#     'G': {'B': 2, 'D': 1, 'C': 2},
#     'C': {'G': 2, 'E': 1, 'F': 16},
#     'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
#     'F': {'A': 5, 'E': 2, 'C': 16}}
# unvisited = {node: None for node in nodes} #using None as +inf
# visited = {}
# current = 'B'
# currentDistance = 0
# unvisited[current] = currentDistance
# while True:
#     for neighbour, distance in distances[current].items():
#         if neighbour not in unvisited: continue
#         newDistance = currentDistance + distance
#         if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
#             unvisited[neighbour] = newDistance
#     visited[current] = currentDistance
#     del unvisited[current]
#     if not unvisited: break
#     candidates = [node for node in unvisited.items() if node[1]]
#     current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
# print(visited)
# =============================================================================
