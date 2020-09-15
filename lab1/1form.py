#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def y(x):
    return np.log( (np.exp(1/(np.sin(x)+1))/(5/4 + 1/(x**15)) ))/np.log(1+x**2)

x = [1, 10, 1000]
for i in x:
    print(y(i), end = ' ')


# In[ ]:




