#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize = (10, 5))
plt.plot(x, np.log(x**2 + 1)/np.log(1 + np.tan(1/(1 + np.sin(x)**2))) * np.exp(-abs(x)/10))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'$f(x)$')
plt.grid(True)
plt.show()


# In[ ]:




