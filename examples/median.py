def median(data):
    sorted_list = sorted(data)
    middle_idx = len(data) // 2
    if len(data) % 2 == 0:
        return (sorted_list[middle_idx - 1] + sorted_list[middle_idx]) * 0.5
    else:
        return sorted_list[middle_idx]
import numpy
numpy.median([])
