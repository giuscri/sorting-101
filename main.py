from typing import List
from random import randint

def partition(A: List[int], pivot: int) -> int:
    i, j = 0, len(A)-1
    while i <= j:
        while i < len(A) and A[i] < pivot:
            i += 1
        while j >= 0 and A[j] >= pivot:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    return i

def quicksort(A: List[int], i: int, n: int) -> None:
    if n-i <= 1:
        return

    pivot_idx = randint(i, n-1)
    pivot = A[pivot_idx]
    start_of_ge_pivot = partition(A, pivot)
    quicksort(A, i, start_of_ge_pivot)
    quicksort(A, start_of_ge_pivot, n)

def merge(A: List[int], B: List[int]) -> List[int]:
    C: List[int] = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1

    while j < len(B):
        C.append(B[j])
        j += 1

    return C

def mergesort(A: List[int]) -> List[int]:
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    A = mergesort(A[:mid])
    B = mergesort(A[mid:])
    return merge(A, B)
