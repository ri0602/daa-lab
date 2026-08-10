import time

while True:

    n = int(input("\nEnter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    start = time.perf_counter_ns()

    # Insertion Sort
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end = time.perf_counter_ns()

    print("Sorted Array:", arr)
    print("Execution Time:", end - start, "ns")

    choice = input("\nDo you want to test another array? (y/n): ")

    if choice.lower() != 'y':
        print("Program Ended.")
        break
    