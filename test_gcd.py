import random
from math import gcd as math_gcd
import pytest
from greatest_common_divider import gcd_range

def naive_gcd_range(arr, L, R):
    g = 0
    for i in range(L, R+1):
        g = math_gcd(g, abs(arr[i]))
    return g

def test_single_element():
    a = [42]
    assert gcd_range(a, 0, 0) == 42

def test_two_elements():
    a = [14, 15]
    assert gcd_range(a, 0, 1) == 1
    assert gcd_range(a, 1, 1) == 15

def test_all_zeros():
    a = [0, 0, 0, 0]
    assert gcd_range(a, 0, 3) == 0
    assert gcd_range(a, 2, 2) == 0

def test_negative_numbers():
    a = [-6, 9, -15]
    assert gcd_range(a, 0, 2) == 3
    assert gcd_range(a, 0, 1) == 3

def test_mixed_zero_and_values():
    a = [0, 12, 18]
    assert gcd_range(a, 0, 2) == 6
    assert gcd_range(a, 1, 2) == 6

class SpyList(list):
    def __init__(self, data):
        super().__init__(data)
        self.read_indices = []

    def __getitem__(self, i):
        self.read_indices.append(i)
        return super().__getitem__(i)

def test_early_exit_behavior():
    # Наличие 1 в диапазоне должно вернуть 1 сразу
    a = SpyList([2, 4, 1, 1000000, 3])
    assert gcd_range(a, 0, 4) == 1
    assert max(a.read_indices) == 2
    assert gcd_range(a, 2, 4) == 1

def test_invalid_ranges():
    a = [1,2,3]
    with pytest.raises(IndexError):
        gcd_range(a, -1, 2)
    with pytest.raises(IndexError):
        gcd_range(a, 0, 3)
    with pytest.raises(IndexError):
        gcd_range(a, 2, 1)

def test_random_small_arrays():
    for _ in range(200):
        n = random.randint(1, 30)
        arr = [random.randint(-200, 200) for _ in range(n)]
        st = random.randint(0, n-1)
        en = random.randint(st, n-1)
        assert gcd_range(arr, st, en) == naive_gcd_range(arr, st, en)

def test_large_values():
    a = [10**18, 10**18 * 2, 10**18 * 3]
    assert gcd_range(a, 0, 2) == 10**18

def test_known_patterns():
    a = [6*i for i in range(1, 21)]
    assert gcd_range(a, 0, 19) == 6
    assert gcd_range(a, 3, 7) == 6

