#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[2]:


os.chdir("C:\\python")
os.getcwd()


# In[3]:


dataset = pd.read_csv("iris.csv")
dataset


# In[4]:


x=dataset.iloc[:,:4].values
x


# In[5]:


y=dataset.iloc[:,4].values
y


# In[16]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
y
from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2)


# In[17]:


from sklearn.neighbors import KNeighborsClassifier


# In[18]:


classifier_knn = KNeighborsClassifier(n_neighbors = 5, metric = "minkowski", p = 2)


# In[19]:


classifier_knn.fit(x_train, y_train)


# In[23]:


Kncl = KNeighborsClassifier()


# In[24]:


Kncl.fit(x_train, y_train)


# In[25]:


y_Pred = Kncl.predict(x_test)


# In[26]:


from sklearn.metrics import confusion_matrix


# In[29]:


confusion_matrix(y_test, y_Pred)


# In[30]:


30/6


# In[ ]:




