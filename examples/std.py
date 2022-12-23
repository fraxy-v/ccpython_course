from mean import mean
import math
def standard_deviation(data):
    m = mean(data)
    sd = 0
    for n in data:
        sd += (n - m)**2
    return math.sqrt( sd / len(data))
