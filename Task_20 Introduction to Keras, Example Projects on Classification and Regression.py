#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[29]:


data = pd.read_csv('C:\\python\\Pima.csv')


# In[31]:


x = data.drop("Outcome", axis=1)


# In[32]:


y = data["Outcome"]


# In[33]:


#Define Model
from keras.models import Sequential


# In[34]:


from keras.layers import Dense


# In[35]:


model = Sequential()


# In[36]:


model.add(Dense(12, input_dim = 8, activation = "relu"))


# In[39]:


model.add(Dense(12, activation = "relu"))


# In[41]:


model.add(Dense(1, activation = "sigmoid"))


# In[42]:


#Compile Model
model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])


# In[43]:


#Training Model
model.fit(x, y, epochs = 150, batch_size = 10)


# In[54]:


#Testing Model
_, accuracy = model.evaluate(x, y)
#accuracy = model.evaluate(x,y)


# In[55]:


print("Model accuracy:  %.2f"% (accuracy*100))


# In[56]:


#Make predictions
predictions = model.predict(x)


# In[60]:


print([round(x[0]) for x in predictions])


# In[61]:


from sklearn.model_selection import train_test_split


# In[64]:


x_test, x_train, y_test, y_train = train_test_split(x,y,test_size = 0.2)


# In[66]:


from sklearn.naive_bayes import GaussianNB


# In[67]:


classifier_NB = GaussianNB()


# In[68]:


classifier_NB.fit(x_train, y_train)


# In[70]:


y_pred = classifier_NB.predict(x_test)


# In[72]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)


# In[73]:


cm = confusion_matrix(y_test, y_pred)
# compute the diagonal sum of the confusion matrix using NumPy
diagonal_sum = np.trace(cm)
total_sum = np.sum(cm)

accuracy = diagonal_sum / total_sum
print("Diagonal sum",diagonal_sum)
print("Diagonal Sum/ Total Sum",accuracy)


# In[ ]:




