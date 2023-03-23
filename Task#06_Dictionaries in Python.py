#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionaries in python
Dict = {1: 'Sukkur', 2: 'IBA', 3: 'University'}
print(Dict)


# In[3]:


#Python dictionary is an ordered collection of items. It stores elements in key/value pairs. 
#Here, keys are unique identifiers that are associated with each value.


cap_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(cap_city)


# In[10]:


#Dictionary Methods

#add Method
# Let's create a dictionary


class my_dictionary(dict):
    def __init__(self):
        self = dict()

# Function to add key:value
    def add(self, key, value):
        self[key] = value


# Main Function
obj = my_dictionary()

obj.add(1, 'Robotics')
obj.add(2, 'Compitition')

print(obj)


# In[14]:


#Method for Removing

dict1 = { "Name": "Dilbar","From": "Sukkur","age": 23}
print(dict1)


# In[15]:


dict1.popitem()
print(dict1)


# In[18]:


#We have also many many methods for dictionaries
#Changing Items 

dict2 = {"Car": "Civic","model": "Corrolla", "year": 2020}
print(dict2)

dict2["year"] = 2023
print(dict2)


# In[ ]:




