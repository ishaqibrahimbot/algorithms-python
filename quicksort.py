"""
Time to implement quicksort now. Let's jot down the overall idea of how quicksort is supposed to work.

1) We select a random pivot in the array

Next, we run the partition subroutine:
2) We place this pivot at the start of the array
3) We compare each subsequent value in the array with the pivot
4) If the value is more than the pivot, we let it be. But if it is less than the pivot, we swap it with
 the left-most entry greater than the pivot
5) We stop once we have compared all values
6) We keep track of the boundary between <p and >p and insert the pivot there at the end

Now we have two subarrays, we send these via recursion through the same process
7) The base case is when we get an array of length 1 or 0, we just return it as is

Now other than this, I need to keep track of the comparisons. This is as simple as just adding (n-1) on 
every recursive call, but now this will be another argument to the function, with an initial value of 0.

"""


# Load the 10,000 integers from the 'Quicksort.txt' file into a list
integer_array = []

with open('Quicksort.txt', 'r') as text_file:
    for row in text_file:
        integer_array.append(int(row))

# Implementation of quicksort that chooses the first element of the array as the pivot
# on each recursive call
def quick_sort_first(array, num_comparisons=0):
    len_arr = len(array)
    if len_arr == 1 or len_arr == 0:
        return array, num_comparisons
    else:
        num_comparisons += (len_arr - 1)

        pivot = array[0]

        pivot_boundary = 1
        counter = 1

        while(counter < len_arr):
            next_value = array[counter]

            if next_value > pivot:
                counter += 1
            else:
                array[counter], array[pivot_boundary] = array[pivot_boundary], array[counter]
                pivot_boundary += 1
                counter += 1

        array[0], array[pivot_boundary-1] = array[pivot_boundary-1], array[0]

        pivot_index = array.index(pivot)

        assert(len(array) == len_arr)

        left_subarray = array[:pivot_index]
        right_subarray = array[pivot_index+1:]

        left_sorted_array, num_comparisons = quick_sort_first(left_subarray, num_comparisons)
        right_sorted_array, num_comparisons = quick_sort_first(right_subarray, num_comparisons)

        new_array = left_sorted_array + [pivot] + right_sorted_array

        return new_array, num_comparisons        

# Quicksort that chooses the last element as the pivot on each recursive call
def quick_sort_last(array, num_comparisons=0):
    len_arr = len(array)
    if len_arr == 1 or len_arr == 0:
        return array, num_comparisons
    else:
        num_comparisons += (len_arr - 1)

        pivot = array[-1]

        array[0], array[-1] = array[-1], array[0]

        # print("pivot = {}".format(pivot))
        # print("array after swapping = {}".format(array))

        pivot_boundary = 1
        counter = 1

        while(counter < len_arr):
            next_value = array[counter]

            if next_value > pivot:
                counter += 1
            else:
                array[counter], array[pivot_boundary] = array[pivot_boundary], array[counter]
                pivot_boundary += 1
                counter += 1

        array[0], array[pivot_boundary-1] = array[pivot_boundary-1], array[0]

        pivot_index = array.index(pivot)

        assert(len(array) == len_arr)

        left_subarray = array[:pivot_index]
        right_subarray = array[pivot_index+1:]

        left_sorted_array, num_comparisons = quick_sort_last(left_subarray, num_comparisons)
        right_sorted_array, num_comparisons = quick_sort_last(right_subarray, num_comparisons)

        new_array = left_sorted_array + [pivot] + right_sorted_array

        return new_array, num_comparisons        

# Uses a "median-of-three" strategy to choose the pivot on every iteration
def quick_sort_median(array, num_comparisons=0):
    len_arr = len(array)
    if len_arr == 1 or len_arr == 0:
        return array, num_comparisons
    else:
        num_comparisons += (len_arr - 1)

        first_element = array[0]
        last_element = array[-1]
        
        if len_arr % 2 == 0:
            middle_element = array[int(len_arr/2)-1]
        else:
            middle_element = array[int(len_arr/2)]

        candidates = [first_element, middle_element, last_element]
        candidates.sort()

        pivot = candidates[1]

        index = array.index(pivot)

        array[0], array[index] = array[index], array[0]

        # print("pivot = {}".format(pivot))
        # print("array after swapping = {}".format(array))

        pivot_boundary = 1
        counter = 1

        while(counter < len_arr):
            next_value = array[counter]

            if next_value > pivot:
                counter += 1
            else:
                array[counter], array[pivot_boundary] = array[pivot_boundary], array[counter]
                pivot_boundary += 1
                counter += 1

        array[0], array[pivot_boundary-1] = array[pivot_boundary-1], array[0]

        pivot_index = array.index(pivot)

        assert(len(array) == len_arr)

        left_subarray = array[:pivot_index]
        right_subarray = array[pivot_index+1:]

        left_sorted_array, num_comparisons = quick_sort_median(left_subarray, num_comparisons)
        right_sorted_array, num_comparisons = quick_sort_median(right_subarray, num_comparisons)

        new_array = left_sorted_array + [pivot] + right_sorted_array

        return new_array, num_comparisons



# sorted_array, num_comparisons = quick_sort_first(integer_array)

# sorted_array, num_comparisons = quick_sort_last(integer_array)

# sorted_array, num_comparisons = quick_sort_median(integer_array)

# print(sorted_array[9900:])
# print(num_comparisons)
