import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 11)
prices = [150, 155, 153, 160, 165, 162, 170, 175, 172, 180]

plt.figure(figsize=(10, 6))
plt.plot(days, prices, marker='o', linestyle='-', color='g')
plt.title("TechCorp Stock Price (Last 10 Days)")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()