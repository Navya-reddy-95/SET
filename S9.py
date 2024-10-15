'''
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
# Input: number of values and then the values themselves
n = int(input("Enter the number of values: "))

# Initialize a list to store the values
values_list = []

# Collect the values from user input
for _ in range(n):
    value = int(input())
    values_list.append(value)

# Use a dictionary to count occurrences of each value
value_count = {}
for value in values_list:
    if value in value_count:
        value_count[value] += 1
    else:
        value_count[value] = 1

# Count the number of duplicate values
duplicate_count = sum(1 for count in value_count.values() if count > 1)

# Get the unique values as a set
unique_values = set(values_list)

# Print the results
print(f"Duplicate Values: {duplicate_count}")
print(" ".join(map(str, sorted(unique_values))) + " ")
