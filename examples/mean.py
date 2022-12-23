def mean(data):
    if len(data) == 0:
        raise ValueError("Empty list")
    sum = 0
    for n in data:
        sum += n
    return sum / len(data)


print(mean([-1,1]))

import numpy

print(numpy.mean([-1,1]))
