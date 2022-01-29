from vectors import *

def test_auto_correlation():
    assert circular_correlation([1, 2, 3], [4, 5, 6]) == [32, 29, 29]

