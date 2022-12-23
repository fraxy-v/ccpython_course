import math
import matplotlib.pyplot as plt
def square_roots(a,b,c):
    d_sqrt = math.sqrt(b**2 - 4*a*c)
    return ((-b + d_sqrt) / (2*a), (-b - d_sqrt) / (2*a))

l = []
for a in range(1,10):
    l.append(square_roots(a,50,3))

plt.plot(l)
plt.show()
