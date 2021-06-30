import numpy as np
import time

def merge_sort_span_indices(indices, starts, ends):
    if len(indices) <= 1:
        return indices
    else:
        n = len(indices)
        A_1 = indices[:int(n/2)]
        # print("A_1 = ", A_1)
        A_2 = indices[int(n/2):]
        # print("A_2 = ", A_2)
        # print()

        A_1_sorted = merge_sort_span_indices(A_1, starts, ends)
        # print("A_1 sorted = ", A_1_sorted)

        A_2_sorted = merge_sort_span_indices(A_2, starts, ends)
        # print("A_2 sorted =", A_2_sorted)

        A_sorted = []

        i = 0
        j = 0

        while(True):

            if starts[A_1_sorted[i]] < starts[A_2_sorted[j]]:
                A_sorted.append(A_1_sorted.pop(i))
            elif starts[A_1_sorted[i]] > starts[A_2_sorted[j]]:
                A_sorted.append(A_2_sorted.pop(j))
            elif ends[A_1_sorted[i]] < ends[A_2_sorted[j]]:
                A_sorted.append(A_1_sorted.pop(i))
            elif ends[A_1_sorted[i]] > ends[A_2_sorted[j]]:
                A_sorted.append(A_2_sorted.pop(j))
            else:
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

#Case 1: Testing start_1 < start_2
# starts = [0, 1, 2, 3, 4, 5]
# ends = [2, 3, 4, 5, 6, 7]
# indices = [5, 4, 3, 2, 1, 0]

# #Case 2: Testing start_2 < start_1
# starts = [0, 1, 2, 3, 4, 5]
# ends = [2, 3, 4, 5, 6, 7]
# indices = [1, 0, 3, 2, 5, 4]

# #Case 3: Testing start_1 = start_2, end_1 < end_2
# starts = [1, 1, 1, 1, 1, 1]
# ends = [5, 4, 3, 2, 1, 0]
# indices = [3, 5, 2, 1, 4, 0]

#Case 4: Testing start_1 = start_2, end_1 = end_2
starts = [1, 1, 1, 1, 1, 1]
ends = [1, 1, 1, 1, 1, 1]
indices = [4, 5, 1, 0, 2, 3]

"""
All test cases have passed!
"""
output = merge_sort_span_indices(indices, starts, ends)
print(output)