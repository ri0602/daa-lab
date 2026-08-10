def merge_sort(arr):

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, left_count = merge_sort(arr[:mid])
    right, right_count = merge_sort(arr[mid:])

    merged, merge_count = merge(left, right)

    total_count = left_count + right_count + merge_count

    return merged, total_count


def merge(left, right):

    result = []

    i = 0
    j = 0
    count = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])

            # All remaining elements in left
            # are greater than right[j]
            count += len(left) - i

            j += 1

    # Add remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result, count


# Input
arr = [8, 4, 2, 1]

# Count inversions
sorted_array, inversions = merge_sort(arr)

print("Array:", arr)
print("Sorted Array:", sorted_array)
print("Number of Inversions:", inversions)