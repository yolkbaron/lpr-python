#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize = (10, 5))
plt.plot(x, eval(input()))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'$f(x)$')
plt.grid(True)
plt.show()


# In[ ]:




