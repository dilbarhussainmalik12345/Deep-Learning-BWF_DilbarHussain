#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Introduction to Numpy
import numpy as np
x = np.array([1, 2, 3, 4])
print("Original Array:")
print(x)
print("Check the array have no any zero element:")
print(np.all(x))
x = np.array([0, 1, 2, 3])
print("Original Array:")
print(x)
print("Check the array have no any zero element:")
print(np.all(x))


# In[3]:


#Practice of Array
#Checking the size
import numpy as np
X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))


# In[4]:


import numpy as np
array=np.arange(30,71)
print("Array of the integers from 30 to70")
print(array)


# In[5]:


#Finding number of rows and columns
import numpy as np
m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the said matrix:")
print(m.shape)


# In[6]:


#Operations on the arrays
import numpy as np
arr1 = np.arange(4, dtype = np.float_).reshape(2, 2)

print('First array\n:')
print(arr1)

print('Second array\n:')
arr2 = np.array([12, 12])
print(arr2)

print('Adding the two arrays\n:')
print(np.add(arr1, arr2))

print('Subtracting the two array\ns:')
print(np.subtract(arr1, arr2))

print('Multiplying the two arrays\n:')
print(np.multiply(arr1, arr2))

print('Dividing the two arrays\n:')
print(np.divide(arr1, arr2))


# In[7]:


import numpy as np
print("Add:")
print(np.add(1.0, 4.0))
print("Subtract:")
print(np.subtract(1.0, 4.0))
print("Multiply:")
print(np.multiply(1.0, 4.0))
print("Divide:")
print(np.divide(1.0, 4.0))


# In[ ]:




