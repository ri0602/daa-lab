def union_intersection(A, B):

    i = 0
    j = 0

    union = []
    intersection = []

    while i < len(A) and j < len(B):

        if A[i] < B[j]:
            union.append(A[i])
            i += 1

        elif A[i] > B[j]:
            union.append(B[j])
            j += 1

        else:
            union.append(A[i])
            intersection.append(A[i])

            i += 1
            j += 1

    # Add remaining elements of A
    while i < len(A):
        union.append(A[i])
        i += 1

    # Add remaining elements of B
    while j < len(B):
        union.append(B[j])
        j += 1

    return union, intersection


# Input arrays
A = [1, 2, 4, 5]
B = [2, 4, 6]

# Find union and intersection
union, intersection = union_intersection(A, B)

# Display results
print("Array A:", A)
print("Array B:", B)
print("Union:", union)
print("Intersection:", intersection)