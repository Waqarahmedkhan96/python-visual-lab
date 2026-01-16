# This below function compares a "slow" algorithm like Bubble Sort $O(n^2)$ to a "fast" one like Python's built-in sort $O(n \log n)$

import matplotlib.pyplot as plt
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sizes = [100, 500, 1000, 1500]
times = []

for s in sizes:
    test_list = [random.randint(0, 1000) for _ in range(s)]
    start = time.time()
    bubble_sort(test_list)
    times.append(time.time() - start)

plt.plot(sizes, times, label="Bubble Sort $O(n^2)$")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity Analysis")
plt.legend()
plt.show()