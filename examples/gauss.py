import math
import matplotlib.pyplot as plt

def gaussian(x, a, z, b = 0):
    return a * math.exp(-z*(x - b)**2)


l = []

x = []
for i in range(0,2000):
    x.append((i - 1000) * 0.01)
    l.append(gaussian(x[i],a=172.25,z=0.0617669))

plt.plot(x, l)
plt.show()
