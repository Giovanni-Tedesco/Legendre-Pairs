import numpy as np

from dft_utils import psd, dft
from vectors import pointwise_op

def sequences_are_compatible(s1, s2) -> bool: 
    psd_s1 = psd(s1)
    psd_s2 = psd(s2)

    print(psd_s1)
    print(psd_s2)

    v = pointwise_op(lambda x, y: x + y, psd_s1, psd_s2)
    # print(v)
    are_almost_equal = lambda x, y: abs(x - y) < 1e-10
    return all([are_almost_equal(v[1], v[i]) for i in range(1, len(v))])


if __name__ == '__main__':
    s_1  = [1, 2, 2, -2, 0, 0, 0]
    s_2  = [2, 1, -1, 2, -1, 0, 0]     


    print(sequences_are_compatible(s_1, s_2))
