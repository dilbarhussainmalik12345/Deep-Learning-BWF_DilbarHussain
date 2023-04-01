#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Starting with pandas
# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("C:\\Users\\Professor Jordan\\Downloads\\nba.csv")

# String to be searched in start of string
search ="G"

# boolean series returned
bool_series = data["College"].str.startswith(search, na = False)


# In[4]:


data[bool_series]


# In[5]:


#Pandas series examples
import pandas as pd

a = [1, 7, 2]

var = pd.Series(a)

print(var)


# In[6]:


print(var[0])


# In[7]:


#Creating labels
import pandas as pd

a = [1, 7, 2]

var = pd.Series(a, index = ["x", "y", "z"])

print(var)


# In[9]:


#Dataframe

import pandas as pd
# Creating a list
author = ['Dilbar', 'Hussain','Bytewise', 'Fellow']
auth_series = pd.Series(author)
# Printing Series
print(auth_series)


# In[10]:


print(type(auth_series))


# In[11]:


# Importing Pandas library
import pandas as pd

# Creating two lists
author = ['Ali', 'Khan','At', 'Sukkur']
article = [210, 211, 114, 178]
# Creating two Series by passing lists
auth_series = pd.Series(author)
article_series = pd.Series(article)
# Creating a dictionary by passing Series objects as values
frame = {'Author': auth_series,'Article': article_series}
# Creating DataFrame by passing Dictionary
result = pd.DataFrame(frame)
# Printing elements of Dataframe
print(result)


# In[ ]:




