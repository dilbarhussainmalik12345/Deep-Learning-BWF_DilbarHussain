#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
import pandas as pd


# In[2]:


os.chdir("C:\\python\\")
os.getcwd()


# In[4]:


data_set = pd.read_csv("iris.csv")
data_set


# In[5]:


x = data_set.iloc[:,:4].values
x


# In[6]:


y = data_set.iloc[:,4].values
y


# In[7]:


from sklearn.preprocessing import LabelEncoder


# In[8]:


lbl = LabelEncoder()


# In[9]:


y = lbl.fit_transform(y)
y


# In[10]:


from sklearn.model_selection import train_test_split


# In[11]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2) 


# In[12]:


from sklearn.neighbors import NearestCentroid


# In[13]:


clf = NearestCentroid()


# In[14]:


clf.fit(x_train, y_train)


# In[16]:


y_pred = clf.predict(x_test)


# In[17]:


from sklearn.metrics import confusion_matrix


# In[18]:


confusion_matrix(y_test, y_pred)


# In[21]:


cm = confusion_matrix(y_test, y_pred)
# compute the diagonal sum of the confusion matrix using NumPy
diagonal_sum = np.trace(cm)
total_sum = np.sum(cm)

accuracy = diagonal_sum / total_sum
print("Diagonal sum:--> ",diagonal_sum)
print("Diagonal Sum/ Total Sum:--> ",accuracy)


# In[ ]:




