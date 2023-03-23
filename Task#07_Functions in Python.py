#!/usr/bin/env python
# coding: utf-8

# In[10]:


#fucntions in python/ definition/ also calling a function
def bytewise():
    print('Hello Hytewise!')

# call the function
bytewise()

print('Outside function')


# In[11]:


def fun():
    print("Hello from Bytewise Fellow")


# In[12]:


fun()


# In[13]:


#DocStrigs
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

square(3)


# In[14]:


#DocString Printing
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
square(6)


# In[15]:


#Passings functions to arguments

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

# function calling
add_numbers(10, 20)


# In[16]:


#Returing Values/with function dfinition
def find_square(num):
    result = num * num
    return result

# function calling
square = find_square(10)

print('Square:',square)


# In[17]:


#Arbitary numbers of Arguments


def add(*num):
    sum = 0;
    for n in num:
        sum = sum + n;
    print("Sum:", sum)

add(3,4,5,6,7)
add(1,2,3,5,6,7,8)


# In[18]:


#Another Example

def Person(*args):
    print(args)

Person('Dilbar Hussain', 'Male', 23, 'Pakistan', +923028563353)


# In[ ]:




