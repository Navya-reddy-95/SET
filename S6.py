'''
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
'''
# Input: a single line of space-separated values
input_values = input("Enter set values separated by space: ")

# Convert the input string into a set of integers
values_set = set(map(int, input_values.split()))

# Print the number of unique elements in the set
print(len(values_set))
