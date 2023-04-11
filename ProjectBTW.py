#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import glob

# loading  and reading all CSV files
csv_files=glob.glob("*.csv")
Frame=[]
for file in csv_files:
    Frame.append(pd.read_csv(file))

us_census=pd.concat(Frame)
print(us_census.head())
# ===============================

# columns convert to their right type (manipulation)
us_census['Income']=pd.to_numeric(us_census['Income'].replace('\$','',regex=True))
us_census['Pacific']=pd.to_numeric(us_census['Pacific'].str.replace('%',''))
us_census['Asian']=pd.to_numeric(us_census['Asian'].str.replace('%',''))
us_census['Hispanic']=pd.to_numeric(us_census['Hispanic'].str.replace('%',''))
us_census['White']=pd.to_numeric(us_census['White'].str.replace('%',''))
us_census['Black']=pd.to_numeric(us_census['Black'].str.replace('%',''))
us_census['Native']=pd.to_numeric(us_census['Native'].str.replace('%',''))
# =================================

# spliting GerderPop into two new column Men and Women
us_census[['Men','Women']]=us_census['GenderPop'].str.split('_',expand=True)

# Removing M and F character and Convert to its right type
us_census['Men']=pd.to_numeric(us_census['Men'].str.replace('[,M]','',regex=True))
us_census['Women']=pd.to_numeric(us_census['Women'].str.replace('[,F]','',regex=True))

x=us_census['Women']
y=us_census['Income']
plt.scatter(x,y)
plt.show()
# ===================================

# filling nan value in column women with total pop per state minus men per state
us_census['Women']=us_census['Women'].fillna(us_census['TotalPop']-us_census['Men'])
print(us_census.duplicated().value_counts())
us_census=us_census.drop_duplicates()
#  ===================================

# scatterplot that shows average income in a state vs proportion of women in that state
plt.scatter(us_census['Women']/us_census['TotalPop'],us_census['Income'])
plt.xlabel('Porportion of Women')
plt.ylabel('Average Income')
plt.show()
# =======================================

# filling up missing value with 0's in the following given column
us_census=us_census.fillna(value={'Asian':0,'Black':0,'White':0,'Pacific':0,'Hispanic':0,'Native':0})
# ======================================

# All Histogram
plt.hist(us_census['Asian'],color='Purple')
plt.xlabel('%age of Asian Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Black'],color='red')
plt.xlabel('%age of Black Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['White'],color='orange')
plt.xlabel('%age of White Population')
plt.ylabel('count')
plt.show()
 
plt.hist(us_census['Native'],color='grey')
plt.xlabel('%age of Native Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Hispanic'],color='Blue')
plt.xlabel('%age of Hispanic Population')
plt.ylabel('count')
plt.show()

plt.hist(us_census['Pacific'],color='green')
plt.xlabel('%age of Pacific Population')
plt.ylabel('count')
plt.show()

