test_dict = {
    'Codingal' : 3,
    'is' : 3 ,
    'best' : 3 ,
    'for' : 3 ,
    'Coding' : 1 ,
}

value = 3
result = 0


for key in test_dict:
    if test_dict[key] == 3:
     result = result + 1


print("Frequency of 3 is" + str(result))