"""
This file implements the merge sort algorithm.

Merge Sort: Given an array A of length n, sort all its elements in ascending order.

Brainstorm:
- Function starts by breaking array into 2 parts and calling merge on each part.
- Base case is when length of array is either 0 or 1, in that case just returns the elements
- The 'merge' part of this just takes the 2 arrays returned and compares the first elements
and puts them in that order.
"""

import numpy as np
import time


A = np.random.randint(1, 100000000, 50000)
A = list(A)

def merge_sort(array_A):
    if len(array_A) <= 1:
        return array_A
    else:
        n = len(array_A)
        A_1 = array_A[:int(n/2)]
        # print("A_1 = ", A_1)
        A_2 = array_A[int(n/2):]
        # print("A_2 = ", A_2)
        # print()

        A_1_sorted = merge_sort(A_1)
        # print("A_1 sorted = ", A_1_sorted)

        A_2_sorted = merge_sort(A_2)
        # print("A_2 sorted =", A_2_sorted)

        A_sorted = []

        i = 0
        j = 0

        while(True):

            if A_1_sorted[i] < A_2_sorted[j]:
                A_sorted.append(A_1_sorted.pop(i))
            else:
                A_sorted.append(A_2_sorted.pop(j))

            if len(A_1_sorted) == 0:
                for x in A_2_sorted:
                    A_sorted.append(x)
                break
            elif len(A_2_sorted) == 0:
                for x in A_1_sorted:
                    A_sorted.append(x)
                break
            else:
                continue


        return A_sorted

a = time.time()
x = merge_sort(A)
b = time.time()

print("Time taken to merge sort = {}".format(b-a))