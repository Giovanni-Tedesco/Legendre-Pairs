import numpy as np


def dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))
