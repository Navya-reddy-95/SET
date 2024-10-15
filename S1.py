'''
 Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
Note: There is trailing space at the end of output
'''
# Read the number of values
n = int(input("Enter the number of values: "))

# Initialize an empty set
values_set = set()

# Get n values in separate lines
for _ in range(n):
    value = int(input())
    values_set.add(value)

# Convert the set to a sorted list
sorted_values = sorted(values_set)

# Print the values with space separation and a trailing space
print(" ".join(map(str, sorted_values)) + " ")
