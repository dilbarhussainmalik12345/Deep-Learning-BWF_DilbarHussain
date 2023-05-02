#!/usr/bin/env python
# coding: utf-8

# In[31]:


import os
import pandas as pd
import numpy as np


# In[32]:


os.chdir("C:\\python")
os.getcwd()


# In[33]:


dataset = pd.read_csv("iris.csv")
dataset


# In[34]:


x=dataset.iloc[:,:4].values
x


# In[35]:


y=dataset.iloc[:,4].values
y


# In[36]:


from sklearn.preprocessing import LabelEncoder


# In[37]:


lbl = LabelEncoder()


# In[38]:


y = lbl.fit_transform(y)
y


# In[39]:


from sklearn.model_selection import train_test_split


# In[40]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)


# In[41]:


from sklearn.linear_model import LogisticRegression


# In[42]:


lgmodel = LogisticRegression()


# In[43]:


lgmodel.fit(x_train, y_train)


# In[44]:


y_pdt = lgmodel.predict(x_test)


# In[45]:


from sklearn.metrics import confusion_matrix


# In[53]:


confusion_matrix(y_test, y_pdt)


# In[59]:


cm = confusion_matrix(y_test, y_pdt)
# compute the diagonal sum of the confusion matrix using NumPy
diagonal_sum = np.trace(cm)
total_sum = np.sum(cm)

accuracy = diagonal_sum / total_sum
print("Diagonal sum",diagonal_sum)
print("Diagonal Sum/ Total Sum",accuracy)
#28/30

