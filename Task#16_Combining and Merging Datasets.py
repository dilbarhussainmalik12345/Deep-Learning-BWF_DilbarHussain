#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Merging dataFrames
import pandas as pd
# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],'Name': ['ABC', 'PQR', 'DEF', 'GHI']})

# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})


frames = [df1, df2]

result = pd.concat(frames)
display(result)


# In[2]:


#Joing dataFrames
import pandas as pd

df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],'Name': ['ABC', 'PQR', 'DEF', 'GHI']})

df3 = pd.DataFrame({'City': ['MUMBAI', 'PUNE', 'MUMBAI', 'DELHI'],'Age': ['12', '13', '14', '12']})

# the default behaviour is join='outer'
# inner join

result = pd.concat([df1, df3], axis=1, join='inner')
display(result)


# In[5]:


#Merging dataFrames
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)


frames = [df1, df2, df3]

result = pd.concat(frames)
print(result)
print(frames)


# In[6]:


#Reshaping in Python
# importing numpy
import numpy as np

# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# printing array
print("Array : " + str(array))

# length of array
n = array.size

# N-D array N dimension
N = 4

# calculating M
M = n//N

# reshaping numpy array
# converting it to 2-D from 1-D array
reshaped1 = array.reshape((N, M))

# printing reshaped array
print("First Reshaped Array : ")
print(reshaped1)

# creating another reshaped array
reshaped2 = np.reshape(array, (2, 8))

# printing reshaped array
print("Second Reshaped Array : ")
print(reshaped2)


# In[ ]:




