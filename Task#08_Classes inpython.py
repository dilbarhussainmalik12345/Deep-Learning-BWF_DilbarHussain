#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Classes in Python
class Bike:
    name = ""
    gear = 0
    
#create class object
bike1 = Bike()

#access attribute and assign new values
bike1.gear = 11
bike1.name = "Racer"

print("Name:  {bike1.name, Gear:  bike1.gear }")


# In[7]:


#inheritance example
class Animal:
    name = ""
    
    def eat(self):
        print("I can eat")
        
#inherit from animal

class Dog(Animal):
    
    # access name attribute of superclass using self
    def display(self):
        
        print("My name is ", self.name)
        
#creating object of sb class
labrador = Dog()
    # access superclass attribute and method
    
labrador.name = "Lebra"
labrador.eat()
    
    #call subclass method 
labrador.display()


# In[ ]:




