def merge_sort(arr):

    # If array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide the array
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare elements from both arrays
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Input
arr = [9, 3, 7, 1, 6]

# Sort the array
sorted_array = merge_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", sorted_array)