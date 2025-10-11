start = 1
end = 10


squares = [num ** 2 for num in range(start, end + 1)]


even_squares = [value for value in squares if value % 2 == 0]
odd_squares = [value for value in squares if value % 2 != 0]


print("All Square Values:", squares)
print("Even Square Values:", even_squares)
print("Odd Square Values:", odd_squares)