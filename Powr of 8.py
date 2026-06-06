def power8(number):

    while number % 8 == 0:
        number = number // 8

    if number == 1:
        return 1
    return 0

number = int(input("Enter the number : "))

if(power8(number)):
    print("\nThe number is power of 8")
else:
    print("\nThe number is not power of 8")