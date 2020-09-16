import numpy as np
import matplotlib.pyplot as plt

def fWeier(a, b, x):
    ans = 0.0
    for i in range(600):
        ans += (b**i)*np.cos((a**i)*np.pi*x)
    return ans

a, b = [float(i) for i in input().split(' ')]
x = np.arange(-2, 2.00001, 0.00001)
plt.figure(figsize = (10, 5))
plt.plot(x, fWeier(a, b, x))
plt.xlabel(r'$x$')
plt.title(r'$Weierstrass$')
plt.show()
plt.savefig('Weierstrass_function.png')
