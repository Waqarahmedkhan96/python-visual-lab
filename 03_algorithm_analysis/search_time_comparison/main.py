import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
linear = n           # O(n)
binary = np.log2(n)  # O(log n)

plt.plot(n, linear, label="Linear Search $O(n)$")
plt.plot(n, binary, label="Binary Search $O(\log n)$")
plt.fill_between(n, linear, binary, color='gray', alpha=0.2)
plt.title("Search Algorithm Efficiency")
plt.legend()
plt.show()