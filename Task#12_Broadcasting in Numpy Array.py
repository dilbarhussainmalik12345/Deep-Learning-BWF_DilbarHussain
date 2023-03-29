#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Broadcasting with numpy
import numpy as np

a = np.array([5, 7, 3, 1])
b = np.array([90, 50, 0, 30])
#For Multiplication dimensions must be same
c = a * b
print(c)


# In[2]:


import numpy as np
a = np.array([17, 11, 19]) 
print(a)
b = 3
print(b)

# Broadcasting happened because of
# miss match in array Dimension.
c = a + b
print(c)


# In[3]:


import numpy as np
A = np.array([[11, 22, 33], [10, 20, 30]])
print(A)
b = 4
print(b)

C = A + b
print(C)


# In[ ]:




