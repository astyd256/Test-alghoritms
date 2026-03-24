import random
import pytest

from lowest_sum import lowest_sum  # замените your_module на имя файла с функцией

def test_empty_array_raises():
    with pytest.raises(ValueError):
        lowest_sum([])

def test_single_element_returns_value():
    assert lowest_sum([7]) == 7

def test_two_elements():
    assert lowest_sum([5, 3]) == 8
    assert lowest_sum([3, 5]) == 8
    assert lowest_sum([-2, 10]) == 8

def test_all_positive():
    arr = [10, 1, 5, 2, 7]
    assert lowest_sum(arr) == 3

def test_with_negatives():
    arr = [4, -5, 2, -3, 10]
    assert lowest_sum(arr) == -8

def test_with_duplicates():
    arr = [2, 2, 2, 2]
    assert lowest_sum(arr) == 4

def test_sorted_input():
    assert lowest_sum([1, 2, 3, 4]) == 3
    assert lowest_sum([4, 3, 2, 1]) == 3

def test_large_values():
    a = 10**18
    b = 10**18 + 1
    assert lowest_sum([a, b, 2*a]) == a + b

def test_random_small_arrays():
    for _ in range(200):
        n = random.randint(1, 30)
        arr = [random.randint(-500, 500) for _ in range(n)]
        # Наивная проверка: перебор всех пар O(n^2)
        if len(arr) == 1:
            expected = arr[0]
        else:
            expected = min(arr[i] + arr[j] for i in range(len(arr)) for j in range(i+1, len(arr)))
        assert lowest_sum(arr) == expected
