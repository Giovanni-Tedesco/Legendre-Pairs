from typing import *
import numpy as np


def dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))

def pointwise_op(f, *x) :
    return [f(*v_i) for v_i in zip(*x)]

def correlation(x, y):
    pass

def circular_correlation(x, y):
    l = len(x)
    ret = []
    for j in range(l):
        s = 0
        for i in range(l):
            s += x[i] * y[(i + j) % l]
        
        ret.append(s)
    
    return ret

def auto_circular_correlation(x):
    return circular_correlation(x, x)