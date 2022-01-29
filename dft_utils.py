import numpy as np

from cmath import exp, pi

# def roots_of_unity(k: complex, n: complex) -> list(complex):
#     return [exp(2j * pi * k * m / n) for m in range(n)]
def roots_of_unity(k: complex, n: complex, l): 
    return exp(2j * pi * k * n/ l)

# This can definitely be improved
def dft(sequence):
    l = len(sequence)
    ret = []
    for k in range(l):
        s = complex(0, 0)
        for n in range(l):
            print(sequence[n])
            s += sequence[n] * roots_of_unity(k, n, l)
        
        ret.append(s)
        
    return ret

def psd(sequence):
    seq = dft(sequence)

    return [x_i.real * x_i.real + x_i.imag * x_i.imag for x_i in seq]



if __name__ == '__main__':
    print(psd([1, 2, 2, -2, 0, 0, 0]))
