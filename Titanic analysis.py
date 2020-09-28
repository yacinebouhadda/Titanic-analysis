#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[4]:


data = pd.read_excel('titanic_dataset.xls')


# In[6]:


data.shape


# In[8]:


data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'],axis=1)


# In[10]:


data.describe()


# In[11]:


data= data.dropna(axis = 0)


# In[12]:


data.shape


# In[13]:


data['pclass'].value_counts()


# In[16]:


data['pclass'].value_counts().plot.bar()


# In[19]:


data.groupby(['sex','pclass']).mean()


# In[24]:


data['age']


# In[25]:


data[data['age'] < 18].groupby(['sex','pclass']).mean()


# In[28]:


data.iloc[0 : 3,0:3]


# In[37]:


data.loc[0:100 , ['age','sex'] ]


# In[ ]:




