# Array Problems:


# Homeworks
# Problem 3:
# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]


def find_k_largest(a, k):
    # Sort the array
    a.sort()
    # Return the last k elements
    return a[-k:]

a = [5, -2, 3, 1, 8, 21, 4, 7]
k = 3
print(find_k_largest(a, k))