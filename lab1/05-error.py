import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-1, 8.01, 0.01)
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
g, w = np.polyfit(x, y, deg=2, cov=True)
p_f = np.poly1d(p)
g_f = np.poly1d(g)
plt.figure(figsize = (10, 5))
plt.plot(t, p_f(t), label=r'$P_1(t) = a_1+b_1t$')
plt.plot(t, g_f(t), label=r'$P_2(t) = a_2+b_2t+c_2t^2$')
plt.errorbar(x, y, xerr = 0.05, yerr = 0.1, fmt = 'none')
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='best', fontsize=12)
plt.grid(True)
plt.show()
