def search_rotated_array(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # Check if left half is sorted
        if arr[left] <= arr[mid]:

            # Target lies in left sorted half
            if arr[left] <= target < arr[mid]:
                right = mid - 1

            # Target lies in right half
            else:
                left = mid + 1

        # Otherwise, right half is sorted
        else:

            # Target lies in right sorted half
            if arr[mid] < target <= arr[right]:
                left = mid + 1

            # Target lies in left half
            else:
                right = mid - 1

    return -1


# Input
arr = [6, 7, 8, 1, 2, 3, 4]
target = 2

# Search
result = search_rotated_array(arr, target)

print("Array:", arr)
print("Target:", target)
print("Index:", result)