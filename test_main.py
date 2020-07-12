from .main import mergesort, partition, quicksort, merge
from typing import List
from random import randint

def check_partition(A: List[int], pivot: int, i: int) -> None:
    assert i in range(len(A))
    for a in A[:i]:
        assert a < pivot
    for a in A[i:]:
        assert a >= pivot

def test_partition():
    A = [1, 5, 3, 1]
    pivot = 2
    i = partition(A, pivot)
    check_partition(A, pivot, i)

def test_partition_with_empty_list():
    i = partition([], 100)
    assert i == 0

def test_partition_with_negative_pivot():
    A = [1, 5, 3, 1]
    pivot = -100
    i = partition(A, pivot)
    check_partition(A, pivot, i)

def test_quicksort():
    A = [246, 55, 261, 1000, 649, 527, 181, 26, 37, 960]
    quicksort(A, 0, len(A))
    assert A == sorted(A)

def test_merge():
    A = [260, 265, 408, 457, 464]
    B = [437, 559, 586, 626, 808]
    C = merge(A, B)
    assert C == sorted(A + B)

def test_mergesort():
    A = [246, 55, 261, 1000, 649, 527, 181, 26, 37, 960]
    A = mergesort(A)
    assert A == sorted(A)
