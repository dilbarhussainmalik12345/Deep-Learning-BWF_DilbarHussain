#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[2]:


os.chdir("C:\\python")


# In[4]:


os.getcwd()


# In[5]:


d_set = pd.read_csv("iris.csv")


# In[6]:


d_set


# In[13]:


x = d_set.iloc[:,:4].values


# In[14]:


x


# In[15]:


y = d_set.iloc[:,4].values
y


# In[16]:


from sklearn.preprocessing import LabelEncoder


# In[17]:


l_bl = LabelEncoder()


# In[18]:


y = l_bl.fit_transform(y)
y


# In[26]:


from sklearn.model_selection import train_test_split


# In[27]:


x_test, x_train, y_test, y_train = train_test_split(x,y,test_size = 0.2)


# In[28]:


from sklearn.naive_bayes import GaussianNB
classifier_NB = GaussianNB()


# In[29]:


classifier_NB.fit(x_train, y_train)


# In[30]:


y_Pred = classifier_NB.predict(x_test)


# In[34]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_Pred)


# In[35]:


113/44


# In[ ]:




