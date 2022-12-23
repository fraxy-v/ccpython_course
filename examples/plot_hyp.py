import math
import matplotlib.pyplot as plt


def quadratic_eq(x,a,b,c):
    return a*x**2 + b*x + c

l = []
for x in range(-150,100):
    l.append(quadratic_eq(x,a=1,b=50,c=2))

plt.plot(l)
plt.show()
