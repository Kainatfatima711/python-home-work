import random
import string


length = int(input("Enter the desired password length: "))


characters = string.ascii_lowercase + string.ascii_uppercase + string.digits


password = ''.join(random.choice(characters) for _ in range(length))


password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

print("Your Random Password is:", final_password)