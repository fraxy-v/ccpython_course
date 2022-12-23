import math
import matplotlib.pyplot as plt
from gauss import gaussian
l = []
x = []
for i in range(0,2000):
    x.append((i - 1000) * 0.01)
    s1 = gaussian(x[i],a=172.25,z=0.0617669)
    s2 = gaussian(x[i],a=25.9109,z=0.358794)
    s3 = gaussian(x[i],a=5.53335,z=0.700713)
    l.append(s1 + s2 + s3)

plt.plot(x, l)
plt.show()
