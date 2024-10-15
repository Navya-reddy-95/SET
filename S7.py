'''
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
# Input: a single line of space-separated values
input_values = input("Enter set values separated by space: ")

# Convert the input string into a set of integers
values_set = set(map(int, input_values.split()))

# Find the maximum and minimum values in the set
max_value = max(values_set)
min_value = min(values_set)

# Print the results
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
