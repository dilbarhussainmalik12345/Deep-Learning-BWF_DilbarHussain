#!/usr/bin/env python
# coding: utf-8

# In[51]:


import os
import pandas as pd
import numpy as np


# In[52]:


os.chdir("C:\\python")


# In[53]:


os.getcwd()


# In[54]:


da_set = pd.read_csv("rainfall_pak.csv")
da_set


# In[55]:


x = da_set.iloc[:,:2].values
x


# In[56]:


y = da_set.iloc[:,2].values
y


# In[57]:


from sklearn.preprocessing import LabelEncoder


# In[58]:


label = LabelEncoder()


# In[59]:


y = label.fit_transform(y)


# In[60]:


y


# In[61]:


from sklearn.model_selection import train_test_split


# In[62]:


x_test, x_train, y_test, y_train = train_test_split(x,y,test_size = 0.2)


# In[63]:


from sklearn.linear_model import LogisticRegression


# In[64]:


lo_mdl = LogisticRegression()


# In[65]:


lo_mdl.fit(x_train, y_train)


# In[66]:


y_pred = lo_mdl.predict(x_test)


# In[67]:


from sklearn.metrics import confusion_matrix


# In[68]:


confusion_matrix(y_test, y_pred)


# In[70]:


cm = confusion_matrix(y_test, y_pred)
# compute the diagonal sum of the confusion matrix using NumPy
diagonal_sum = np.trace(cm)
total_sum = np.sum(cm)

accuracy = diagonal_sum / total_sum
print("Diagonal sum",diagonal_sum)
print("Total Sum", total_sum)
print("Diagonal Sum/ Total Sum",accuracy)


# In[ ]:




