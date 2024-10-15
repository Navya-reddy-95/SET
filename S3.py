'''
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.
'''
# Input: a line of space-separated values and the element to delete
input_values = input("Enter set values separated by space: ")
element_to_delete = int(input("Enter the value to delete: "))

# Convert the input string into a set of integers
values_set = set(map(int, input_values.split()))

# Check if the element is in the set and delete it if it is
if element_to_delete in values_set:
    values_set.remove(element_to_delete)
    # Convert the set to a sorted list for output
    sorted_values = sorted(values_set)
    # Print the remaining values with space separation and a trailing space
    print(" ".join(map(str, sorted_values)) + " ")
else:
    print("Given value is not present in the set list.")
