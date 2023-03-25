#!/usr/bin/env python
# coding: utf-8

# In[65]:


#Reading file in python
file1 = open("task9.txt")
#0r


# In[66]:


file1 = open("task9.txt", "r")


# In[67]:


#Read file
# read the file
read_content = file1.read()
print(read_content)


# In[68]:


with open('task9.txt', 'w') as file1:

    # write contents to the test2.txt file
    file1.write('I am bytewise fellow dilbar hussain.')
    file1.write('Programiz for beginners')


# In[69]:


#Using Try...
try:
    file1 = open("task9.txt", "r")
    read_content = file1.read()
    print(read_content)
except:
    print("Something went wrong")
finally:
    # close the file
    file1.close()

