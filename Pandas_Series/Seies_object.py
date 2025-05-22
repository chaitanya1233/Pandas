import pandas as pd
import numpy as np
print('Hello User , wecome to my Repository')

s  = pd.Series([1,2,3,4],index = ['a','b','c','d'])
# print(s)

# Seies is like a  numpy ndarray
s2 = pd.Series(np.random.randn(3),index = ['a','b','c'])
# print(s2)

# Create a series object by passing a list 
print('This is my series objet of List')
s_list = pd.Series([10,20,30,40])
print(s_list)

# Oprations on the list.

# 1 . what are is the indexes of the series object.
print(s_list.index)

print(f'Maximum element form the series object is {s_list.max()}')
print(f'Mminimum element form the series object is {s_list.min()}')
print(f'Mean of series object data is {s_list.mean()}')
print(f'Medain of series object data is  {s_list.median()}')

# print(f'The mode of the series data is ({s_list.mode()}')

