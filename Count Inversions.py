"""
This scratch file implements an algorithm to count the number of inversions in an array of size n.

An inversion is defined as a pair of (i,j) indices from an array where A[i]>A[j].

Note: This algorithm makes full use of the fact that an array, when sorted recursively,
automatically uncovers inversions between two smaller arrays.

"""
integer_array = []

with open('IntegerArray.txt', 'r') as text_file:
    for row in text_file:
        integer_array.append(int(row))

# print(len(integer_array))
# print(integer_array[:20])

# A = [0, 9, 1, 8, 2, 7, 3, 6, 4, 11, 5]


def count_inversions(array):
    n = len(array)

    #Base case
    if n <= 1:
        return 0, array

    else:
        array_1 = array[:int(n/2)]
        array_2 = array[int(n/2):]

        left_inv, sorted_1 = count_inversions(array_1)
        right_inv, sorted_2 = count_inversions(array_2)

        # print("left inv = {}, sorted_1 = {}".format(left_inv, sorted_1))
        # print("right inv = {}, sorted_2 = {}".format(right_inv, sorted_2))

        A_sorted = []
        i = 0
        j = 0
        total_inversions = left_inv + right_inv

        while(True):
            if sorted_1[i] < sorted_2[j]:
                total_inversions += 0
                A_sorted.append(sorted_1[i])
                i+=1

            elif sorted_1[i] > sorted_2[j]:
                total_inversions += len(array_1[i:])
                A_sorted.append(sorted_2[j])
                j+=1

            if i == len(sorted_1):
                for x in range(j, len(sorted_2)):
                    A_sorted.append(sorted_2[x])
                break

            if j == len(sorted_2):
                for x in range(i, len(sorted_1)):
                    A_sorted.append(sorted_1[x])
                break

        return total_inversions, A_sorted


inv, array = count_inversions(integer_array)
print(inv)
