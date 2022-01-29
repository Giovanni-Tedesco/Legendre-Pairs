import numpy as np

from cmath import exp, pi

# def roots_of_unity(k: complex, n: complex) -> list(complex):
#     return [exp(2j * pi * k * m / n) for m in range(n)]
def roots_of_unity(k: complex, l): 
    return exp(2j * pi * k / l)

def dft(sequence):
    l = len(sequence)
    ret = []
    for k in range(l):
        s = 0
        for n in range(l - 1):
            s += sequence[n] * roots_of_unity(1j * k, l)
        
        ret.append(np.real(s))
    
    return ret

def psd(sequence):
    return [i**2 for i in sequence]

if __name__ == '__main__':
    print(psd(dft([1, 2, 2, -2, 0, 0, 0])))