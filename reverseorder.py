number = int(input("Enter a number : "))
count = 0

while number != 0 :
    digit = number % 10 
    number = number // 10
    count += 1
    print("Total digits:", count)