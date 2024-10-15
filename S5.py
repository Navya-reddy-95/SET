'''
 Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''
# Input: two lines of space-separated values
input_values1 = input("Enter the first set of values separated by space: ")
input_values2 = input("Enter the second set of values separated by space: ")

# Convert the input strings into sets of integers
set1 = set(map(int, input_values1.split()))
set2 = set(map(int, input_values2.split()))

# Find the intersection of the two sets
common_values = set1 & set2  # or set1.intersection(set2)

# Convert the common values to a sorted list
sorted_common_values = sorted(common_values)

# Print the common values with space separation and a trailing space
print(" ".join(map(str, sorted_common_values)) + " ")
