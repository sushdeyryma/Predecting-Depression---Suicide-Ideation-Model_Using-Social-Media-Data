#!/usr/bin/env python
# coding: utf-8

# # NO_Code_only_Output

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[ ]:





# In[2]:


Dataset = pd.read_csv('Count_vectorizer.csv')


# In[3]:


Dataset


# In[4]:


sns.barplot(x = 'Features', y = 'Accuracy',hue = "Algorithms", data = Dataset);


# In[5]:


sns.barplot(x = 'Features', y = 'f1-score',hue = "Algorithms", data = Dataset);

