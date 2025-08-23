# Project: Circumference of a Circle

def circumference(radius):
    return 2 * 3.14159 * radius   # Formula: 2πr

# Ask user for input
r = float(input("Enter the radius of the circle: "))

# Call the function and show result
print("The circumference of the circle is:", circumference(r))