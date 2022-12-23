import math
import matplotlib.pyplot as plt
from gauss import gaussian

l = []
x = []
for i in range(0,2000):
    x.append((i - 1000) * 0.01)
    s1 = gaussian(x[i],a=172.25,z=0.617669, b = -5)
    s2 = gaussian(x[i],a=172.25,z=0.617669, b = 5)
    l.append(s1 * s2)

plt.plot(x, l)
plt.show()
