# problem 4:
# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]


def find_closest_sum(a, b, t):
    # Initialize the closest sum
    closest_sum = a[0] + b[0]
    # Initialize the closest pair
    closest_pair = [a[0], b[0]]
    # Loop through the first array
    for i in range(len(a)):
        # Loop through the second array
        for j in range(len(b)):
            # Calculate the sum
            sum = a[i] + b[j]
            # Check if the sum is closer to the target
            if abs(t - sum) < abs(t - closest_sum):
                # Update the closest sum
                closest_sum = sum
                # Update the closest pair
                closest_pair = [a[i], b[j]]
    # Return the closest pair
    return closest_pair

a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=20
print(find_closest_sum(a, b, t))