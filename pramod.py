#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.graph_objects as go


# In[5]:


# Import Dataset Sources
df=pd.read_excel('Global .xlsx')


# In[4]:


# LOad The Data
df.head()


# In[16]:


# Finding Number of Rows and Columns
df.shape


# In[17]:


# Find Basic Information about Data
df.info()


# In[18]:


# Finding Duplicate Values
df.duplicated().sum()


# In[19]:


# Finding All Null values in the data
df.isnull().sum()


# In[20]:


# Finding unique Numbers
df.nunique()


# In[21]:


df=df.drop(['Row ID','Order ID','Customer ID','Postal Code','Product ID'],axis=1)


# In[22]:


df.head()


# In[23]:


# Checking what are the different type columns are there
df.columns


# In[24]:


# Pairplot Analysis of BASED ON CATEGORY
sns.pairplot(df, hue=('Category'))


# In[25]:


df.head()


# In[26]:


#Viewing Specific Statistcs metrix
df.describe()


# In[27]:


df1=df.corr()


# In[28]:


# Boxplot Visualisation
plt.figure(figsize=(5,10))
sns.boxplot(data=df1)


# In[20]:


# Countplot of Each Columns
fig,axs=plt.subplots(nrows=2,ncols=2,figsize=(10,10))
sns.countplot(df['Category'],ax=axs[0][0])
sns.countplot(df['Segment'],ax=axs[0][1])
sns.countplot(df['Region'],ax=axs[1][0])
sns.countplot(df['Ship Mode'],ax=axs[1][1])
axs[0][0].set_title('category')
axs[0][1].set_title('Segment')
axs[1][0].set_title('Region')
axs[1][1].set_title('Ship Mode')


# In[42]:


# Sub category Analysis
plt.figure(figsize=(15,10))
sns.countplot(df['Sub-Category'])
plt.title('Sub-Category',fontsize=10)


# In[59]:


df.head()


# In[31]:


(df['Sales']).plot.line()
plt.title('Sales',fontsize=20)


# In[5]:


plt.figure(figsize=(10,3))
sns.countplot(df['Discount'])
plt.title('Discount',fontsize=20)


# In[5]:


plt.figure(figsize=(10,3))
sns.countplot(df['Quantity'])
plt.title('Quantity',fontsize=20)


# In[33]:


# Corelating the sales and profit
# Maximum the sales(15000) maximumis the profit(8000)
# Negative is the sales(5000 to 10000).minimum is the profit.
sns.scatterplot(df['Profit'], df['Sales'], data=df)


# In[38]:


#orelating the sales and segment
#with the segment Consumer and Corporate,Home office the profit is in profitside and moving upwards
plt.figure(figsize = (10,5))
sns.scatterplot(x='Sales', y='Profit', hue ='Segment',data=df)


# In[6]:


df = pd.pivot_table(df,index = ['Category', 'Sub-Category'], columns='Segment', values ='Sales', aggfunc = np.mean)


# In[7]:


#Compartion of Category and Sub-category
# The segment 'Home office' has higher profit in 1000 with Category; home office Appliance and sub Category; copiers.
# The Corporate segment also higher profit in 950 with category;Tehnology and sub category;copiers
# above the Observation shows that category; Technology in home office has higher profit with 1000

df.plot(kind = 'bar')


# In[ ]:




