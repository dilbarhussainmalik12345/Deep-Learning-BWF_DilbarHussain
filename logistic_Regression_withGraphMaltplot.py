#!/usr/bin/env python
# coding: utf-8

# In[77]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[78]:


os.chdir('C:\\python')
os.getcwd()


# In[79]:


dataset = pd.read_csv('iris.csv')
dataset


# In[80]:


x = np.array([0,5])
y = np.array([0, 150])


# In[81]:


plt.plot(x, y)
plt.show()


# In[82]:


x = dataset.iloc[:, :4].values
x


# In[83]:


y = dataset.iloc[:,4].values
y


# In[84]:


from sklearn.preprocessing import LabelEncoder


# In[85]:


label = LabelEncoder()


# In[86]:


y = label.fit_transform(y)
y


# In[87]:


from sklearn.model_selection import train_test_split


# In[88]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)


# In[89]:


from sklearn.linear_model import LogisticRegression


# In[90]:


lmdl = LogisticRegression()


# In[91]:


lmdl.fit(x_train, y_train)


# In[92]:


y_prdt = lmdl.predict(x_test)


# In[93]:


from sklearn.metrics import confusion_matrix


# In[94]:


confusion_matrix(y_test, y_prdt)


# In[95]:


y_test = np.array([0,3])


# In[96]:


y_prdt = np.array([0, 3])


# In[97]:


plt.plot(y_test, y_prdt)
plt.show


# In[98]:


cm = confusion_matrix(y_test, y_prdt)
# compute the diagonal sum of the confusion matrix using NumPy
diagonal_sum = np.trace(cm)
total_sum = np.sum(cm)

accuracy = diagonal_sum / total_sum
print("Diagonal sum",diagonal_sum)
print("Diagonal Sum/ Total Sum",accuracy)
#28/30


# In[ ]:




