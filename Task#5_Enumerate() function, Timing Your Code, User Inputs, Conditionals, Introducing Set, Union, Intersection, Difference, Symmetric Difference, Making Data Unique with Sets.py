#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))


# In[2]:


#Timing your code
import time

# starting time
start = time.time()

# program body starts
for i in range(10):
    print(i)

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")


# In[3]:


#User input
val = input("Enter your value: ")
print(val)


# In[4]:


#Condition Statements
#If Condition
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')


# In[6]:


#IF Else
number = -1

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')


# In[7]:


#If elif if else
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')


# In[8]:


#In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# In[9]:


#Union in Python
A = {2, 3, 5}
B = {1, 3, 5}

# compute union between A and B
print('A U B = ', A.union(B))


# In[10]:


#Intersection
A = {2, 3, 5}
B = {1, 3, 5}

# compute intersection between A and B
print("Intersection = " ,A.intersection(B))


# In[11]:


#Difference
# sets of numbers
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}

# returns items present only in set A
print("Difference = ",A.difference(B)) 


# In[12]:


# Symmetric Difference
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
result = A.symmetric_difference(B)
print("Symmetric difference is = ",result)


# In[14]:


#Making data unique in sets
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

        for x in unique_list:
            print(x)


# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)


list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)


# In[ ]:




