# Easy Project: Age Counter

try:
    age = int(input("Enter your age: "))

    if age % 2 == 0:
        print("Even Age")
    else:
        print("Odd Age")

except:
    print("Please enter a number only.")