'''
Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
# Input: two lines of space-separated values
input_values1 = input("Enter the first set of values separated by space: ")
input_values2 = input("Enter the second set of values separated by space: ")

# Convert the input strings into sets of integers
set1 = set(map(int, input_values1.split()))
set2 = set(map(int, input_values2.split()))

# Update the first set with the elements from the second set
set1.update(set2)

# Convert the updated set to a sorted list for output
sorted_updated_set = sorted(set1)

# Print the updated set with space separation
print(" ".join(map(str, sorted_updated_set)))
