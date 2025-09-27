import array as arr

# Array with your example values
array_data = arr.array('u', ['1', '2', '3', '3', '4', 'red', 'blue', '3'])

print("Original array: " + str(array_data))

print()
# Count how many times '3' appears
print("Number of occurrences of '3' in the array: " + str(array_data.count('3')))

print()
# Reverse the array
array_data.reverse()
print("Reversed array: " + str(array_data))