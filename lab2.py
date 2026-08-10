import matplotlib.pyplot as plt

# Number of elements
elements = [5, 10, 15, 20, 25]

# Average execution time (Replace with your own values)
time_ns = [1500, 2200, 2900, 3500, 4200]

plt.plot(elements, time_ns, marker='o', color='green')

plt.title("Dutch National Flag Algorithm")
plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (ns)")
plt.grid(True)

plt.show()