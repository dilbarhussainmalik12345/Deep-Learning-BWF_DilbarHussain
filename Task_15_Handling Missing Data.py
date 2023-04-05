#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Handling Missing data
#Import the libraries
import numpy as np
import pandas as pd

# Create a CSV dataset
data_string = '''ID,Gender,Salary,Country,Company
1,Male,15000,India,Google
2,Female,45000,China,NaN
3,Female,25000,India,Google
4,NaN,NaN,Australia,Google
5,Male,NaN,India,Google
6,Male,54000,NaN,Alibaba
7,NaN,74000,China,NaN
8,Male,14000,Australia,NaN
9,Female,15000,NaN,NaN
10,Male,33000,Australia,NaN'''

with open('salary.csv', 'w') as out:
    out.write(data_string)

# Import the dataset
df = pd.read_csv('C:\\python\\abc.csv')
print('Missing Data\n', df.isnull())


# In[8]:


gender = pd.isnull(df["species"])
gender    


# In[9]:


#Import the libraries
import numpy as np
import pandas as pd

# Create a CSV dataset
data_string = '''ID,Gender,Salary,Country,Company
1,Male,15000,India,Google
2,Female,45000,China,NaN
3,Female,25000,India,Google
4,NaN,NaN,Australia,Google
5,Male,NaN,India,Google
6,Male,54000,NaN,Alibaba
7,NaN,74000,China,NaN
8,Male,14000,Australia,NaN
9,Female,15000,NaN,NaN
10,Male,33000,Australia,NaN'''

with open('salary.csv', 'w') as out:
    out.write(data_string)

# Import the dataset
df = pd.read_csv('C:\\python\\abc.csv')

print('Non Missing Data\n', df.notnull())


# In[10]:


#Filling and Replcaing data
import pandas as pd

df = {
"Array_1": [49.50, 70],
"Array_2": [65.1, 49.50]
}

data = pd.DataFrame(df)

print(data.replace(49.50, 60))


# In[13]:


import pandas as pd

data = {
  "name": ["Bill", "Bob", "Betty"],
  "age": [50, 50, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)

newdf = df.replace(50, 60)


# In[14]:


print(newdf)


# In[15]:


#Droping duplicate values
import pandas as pd

data = {
  "name": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}

df = pd.DataFrame(data)

newdf = df.drop_duplicates()

print(newdf)


# In[18]:


df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
print(df)


# In[19]:


#Detect and Removing outliers
# Importing
import sklearn
from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
bos_hou = load_boston()

# Create the dataframe
column_name = bos_hou.feature_names
df_boston = pd.DataFrame(bos_hou.data)
df_boston.columns = column_name
df_boston.head()


# In[ ]:




