#!/usr/bin/env python
# coding: utf-8

# # zomato Data Analysis Project using Python

# # 1) What type of resturant do the majority of customers order from?

# # 2)How many votes has each types of resturant received from customers?
# 

# # 3)What are the ratings that the majority of resturants have received?
# 

# # 4)What is their average spending on each order?
# 

# # 5)Which mode has received the maximum rating?

# # 6)Which type of resturant received more offline orders,so that zomato can offers customers with some good offers?

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # create the dataframe

# In[4]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)


# In[5]:


dataframe


# # convert the data type column-rate

# In[7]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[8]:


dataframe.info()


# # Types of Resturant

# In[9]:


dataframe.head()


# In[10]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of resturant")


# # conclusion-majority of the resturant falls in dining category

# In[17]:


dataframe.head()


# In[20]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="blue", marker="o")
plt.xlabel("Type of resturant", c="red", size=20)
plt.ylabel("votes", c="red", size=20)


# # conclusion-Dinning resturants receives maximum votes

# In[21]:


plt.hist(dataframe['rate'],bins=5)
plt.title("ratings distribution")
plt.show()


# # conclusion-the majority resturant received ratings from 3.5 to 4

# # Average Order Spendings by Couples

# In[22]:


dataframe.head()


# In[23]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # conclusion-The majority of preferr resturants with an approximate cost of 300 rupees

# # Which mode receives maximum rating

# In[25]:


plt.figure(figsize =(6,6))
sns.boxplot(x = 'online_order',y = 'rate', data=dataframe)


# # Conclusion-Offline order received lower rating in comparison to online order

# In[26]:


dataframe.head()


# In[27]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("online order")
plt.ylabel("Listed In (Type)")
plt.show()


# # CONCLUSION-Dinning resturants primarily accept offline orders,whereas cafes primarily receive online orders.This suggests
# 

# # that clients prefer order in person at resturants,but prefer online ordering at cafes.

# In[ ]:




