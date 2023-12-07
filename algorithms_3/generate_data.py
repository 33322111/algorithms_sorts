import numpy as np


def generate_data(size, reversed_order=False, almost_sorted=False):
    data = np.arange(size)
    if reversed_order:
        data = data[::-1]
    elif almost_sorted:
        for _ in range(size // 20):
            i, j = np.random.choice(size, 2, replace=False)
            data[i], data[j] = data[j], data[i]
    np.random.shuffle(data)
    return data
