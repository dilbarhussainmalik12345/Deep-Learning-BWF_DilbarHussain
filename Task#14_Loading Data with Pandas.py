#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Reading CSV File
#Starting with pandas
# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("C:\\Users\\Professor Jordan\\Downloads\\nba.csv")

# String to be searched in start of string
search ="G"

# boolean series returned
bool_series = data["College"].str.startswith(search, na = False)
data[bool_series]


# In[ ]:




