#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install google-play-scraper


# In[3]:


pip install facebook_reviews


# In[6]:


pip install facebook-scraper


# In[11]:


pip install transformers


# In[12]:


pip install plotly-express


# In[13]:


pip install pandas


# In[14]:


import pandas as pd
import numpy as np
from google_play_scraper import app, reviews_all
import plotly.express as px


# In[15]:


facebook_project = reviews_all('com.facebook.katana', sleep_milliseconds=0, country='US')


# In[16]:


facebook_project


# In[17]:


df = pd.json_normalize(facebook_project)


# In[18]:


df.head()


# In[19]:


df['score'].mean()


# In[20]:


df['reviewCreatedVersion'].value_counts()


# In[21]:


df.dtypes


# In[22]:


df.shape

