#!/usr/bin/env python
# coding: utf-8

# In[27]:


import os
import pandas as pd
import numpy as np


# In[28]:


os.chdir("C:\\python")
os.getcwd()


# In[29]:


s_et = pd.read_csv("iris.csv")
s_et


# In[30]:


x = s_et.iloc[:,0:4].values
x


# In[31]:


y = s_et.iloc[:, 4].values


# In[32]:


y


# In[33]:


from sklearn.preprocessing import LabelEncoder


# In[34]:


lbl = LabelEncoder()


# In[35]:


y = lbl.fit_transform(y)
y


# In[36]:


from sklearn.model_selection import train_test_split


# In[40]:


x_test, x_train, y_train, y_test = train_test_split(x,y,test_size = 0.5)


# In[41]:


from sklearn.tree import DecisionTreeClassifier


# In[42]:


classifier_dt = DecisionTreeClassifier(criterion = 'entropy')


# In[43]:


classifier_dt.fit(x_train, y_train)


# In[44]:


y_Pred = classifier_dt.predict(x_test)


# In[45]:


from sklearn.metrics import confusion_matrix


# In[46]:


confusion_matrix(y_test, y_train)


# In[47]:


27/84


# In[ ]:




