#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Multiplication of matrix
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("Original Matrix:--> ")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the matrix after multiplication:--> :")
print(result1)


# In[6]:


#NumPy program to compute the determinant of square array
import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0], [1, 2]])
print("Original 2-D array: ")
print(a)
print("Determinant of the 2-D array:")
print(np.linalg.det(a))


# In[7]:


#mean of the matrix
import numpy as np  
a = np.array([[1, 2], [3, 4]])  
b=np.mean(a)  
print(b) 
x = np.array([[5, 6], [7, 34]])  
y=np.mean(x)  
print(y)  


# In[9]:


#median of the matrix
arr = [12, 7, 15, 8, 9, 5, 3]
arr1 = np.median(arr)
print(arr1)


# In[11]:


#mode of the matix
from scipy import stats as st
import numpy as np
abc = np.array([1, 1, 2, 2, 2, 3, 4, 5])

print(st.mode(abc))


# In[14]:


#mode also
import statistics as st
import numpy as np
arr1 = np.array([9, 8, 7, 6, 6, 6, 6, 5, 5, 4,3, 2, 1, 1, 1, 1, 1, 1])
print(st.mode(arr1))


# In[16]:


#Quartiles
# numpy.quantile() method
import numpy as np

arr = [20, 2, 7, 1, 34]

print("arr : ", arr)
print("Q2 quantile of arr : ", np.quantile(arr, .25))
print("Q1 quantile of arr : ", np.quantile(arr, .40))
print("Q3 quantile of arr : ", np.quantile(arr, .80))
print("100th quantile of arr : ", np.quantile(arr, .30))


# In[21]:


#Rank of the matrix

import numpy

array= numpy.matrix([[8,1,7],[5,2,6]])

print("Original Matrix is:--> ",array)

rank=numpy.linalg.matrix_rank(array)

print("Rank of the Matrix is:--> ", rank)


# In[22]:


#Probability Distribution
from numpy import random
x = random.binomial (n=6, p=0.5, size=10)
print(x)


# In[23]:


#Finding minimum and maximmum elements of the array
#Statical Functions
import numpy as np
arr= np.array([[1,23,78],[98,60,75],[79,25,48]])  
print(arr)
#Minimum Function
print(np.amin(arr))
#Maximum Function
print(np.amax(arr))


# In[24]:


#Standard Deviation
import numpy as np
a = np.array([5,6,7]) 
print(a)
print(np.std(a))


# In[ ]:




