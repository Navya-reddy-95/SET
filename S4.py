'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
'''
# Input: two lines of space-separated values
input_values1 = input("Enter the first set of values separated by space: ")
input_values2 = input("Enter the second set of values separated by space: ")

# Convert the input strings into sets of integers
set1 = set(map(int, input_values1.split()))
set2 = set(map(int, input_values2.split()))

# Find the difference between the two sets
difference = set1 - set2

# Convert the difference to a sorted list
sorted_difference = sorted(difference)

# Print the unique values with space separation and a trailing space
print(" ".join(map(str, sorted_difference)) + " ")
