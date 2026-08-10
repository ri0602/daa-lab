import matplotlib.pyplot as plt

# Number of elements
elements = [5, 10, 15, 20]

# Execution time in nanoseconds
time_ns = [41920,50840,105080,131640]

plt.plot(elements, time_ns, marker='o', linestyle='-', color='blue')

plt.title("Insertion Sort Execution Time")
plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (ns)")
plt.grid(True)

plt.show()