"""
This scratch file will implement the closest pair algorithm.

Brief overview:
- You want to sort the array in 2 ways: Px which are the points sorted by x coordinate,
and Py (points sorted by y coordinate).
- Now, you want to divide it into 2 based on Px. Find the closest pair in 1st and 2nd half recursively.
The base case here is simply using the euclidean distance between 2 points
- Now, you want to send Px and Py and a Delta (min of distance from 1st/2nd halves). You will find the largest
x value in the left half of Px and call that x_bar. You will define S_y which has points ranging from x-x_bar
x+x_bar but sorted based on y-coordinate.
- Finally, you do a simple linear search through Sy for the closest pair
"""

import time, random, math
import matplotlib.pyplot as plt

def euc_diff(a, b):
    x1, y1 = a
    x2, y2 = b

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    return distance
def brute_force(array):
    best_dist = 1000
    closest_pair = None
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == j:
                continue

            dist = euc_diff(array[i], array[j])
            if dist <= best_dist:
                closest_pair = [array[i], array[j]]
                best_dist = dist

    return closest_pair, best_dist
def merge_sort_points(array_A, criteria):
    if len(array_A) <= 1:
        return array_A
    else:
        n = len(array_A)
        A_1 = array_A[:int(n/2)]
        # print("A_1 = ", A_1)
        A_2 = array_A[int(n/2):]
        # print("A_2 = ", A_2)
        # print()

        A_1_sorted = merge_sort_points(A_1, criteria)
        # print("A_1 sorted = ", A_1_sorted)

        A_2_sorted = merge_sort_points(A_2, criteria)
        # print("A_2 sorted =", A_2_sorted)

        A_sorted = []

        i = 0
        j = 0

        while(True):

            if A_1_sorted[i][criteria] < A_2_sorted[j][criteria]:
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
# num = 10000
# points = []
# for i in range(num):
#     points.append((random.randint(-num, num), random.randint(-num, num)))

# print("points = {}".format(points))
# sorted_points = merge_sort_points(points, 1)
# print("unsorted points = {}".format(points))
# print("sorted based on x = {}".format(sorted_points))

# Px = merge_sort_points(points, 0)
# print("Px = {}".format(Px))
# Py = merge_sort_points(points, 1)
# print("Py = {}".format(Py))
def closest_pair(Px):
    n = len(Px)
    # print("n = {}".format(n))

    if n <= 1:
        return Px , 10000000

    else:
        Qx = Px[:int(n/2)]
        # Qy = Py[:int(n/2)]

        Rx = Px[int(n/2):]
        # Ry = Py[int(n/2):]

        pair_Q, dist_q = closest_pair(Qx)

        pair_R, dist_r = closest_pair(Rx)

        # print("Pair q = {}, dist q = {}".format(pair_Q, dist_q))
        # print("Pair r = {}, dist r = {}".format(pair_R, dist_r))

        delta = min(dist_q, dist_r)
        # print("Delta = {}".format(delta))

        x_bar = Qx[-1][0]
        # print("x_bar = {}".format(x_bar))

        x_plus = x_bar + delta
        x_minus = x_bar - delta

        Sy = [point for point in merge_sort_points(Px, 1) if x_minus<=point[0]<=x_plus]
        # print("Sy = {}".format(Sy))
        # print("Length of Sy = {}".format(len(Sy)))

        best = delta
        best_pair = None

        for i in range(0, len(Sy)):
            for j in range(0, min(7, abs(len(Sy)- i))):
                if i == j:
                    continue
                p = Sy[i]
                q = Sy[j]
                distance = euc_diff(p, q)
                if distance < best:
                    best = distance
                    best_pair = [p, q]


        if best_pair is None:
            if dist_r < dist_q:
                return pair_R, dist_r
            else:
                return pair_Q, dist_q
        else:
            return best_pair, best
#
# a = time.time()
# pair, dist = closest_pair(Px)
# b = time.time()
# print("Using closest_pair:\nClosest pair is: {} and {}".format(pair[0], pair[1]))
# print("Distance between points is: {}".format(dist))
# print("Time taken = {}".format(b-a))
#
# c = time.time()
# pair_2, dist_2 = brute_force(points)
# d = time.time()
# print("\nUsing brute force: \nClosest pair is: {} and {}".format(pair_2[0], pair_2[1]))
# print("Distance between points is: {}".format(dist_2))
# print("Time taken = {}".format(d-c))

num_array = []

for num in range(10, 50):
    points = []
    num_array.append(num)
    for i in range(num):
        points.append((random.randint(-num, num), random.randint(-num, num)))

Px = merge_sort_points(points, 0)
a = time.time()
pair, dist = closest_pair(Px)
b = time.time()
closest_pair_time = b-a

c = time.time()
pair_2, dist_2 = brute_force(Px)
d = time.time()
brute_force_time = d - c

print(f"Time taken by closest pair: {closest_pair_time}")
print(f"Time taken by brute force: {brute_force_time}")




#
#
#
#
# before = time.time()

# after = time.time()
#
# print("Closest pairs are: {} and {}".format(pair[0], pair[1]))
# print("Distance is: {}".format(dist))
# print("Time taken to compute: {}".format(after-before))