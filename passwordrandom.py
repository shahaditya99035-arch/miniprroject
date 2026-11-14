import random
import string

length = int(input("How long password do you want? "))
chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(random.choice(chars) for _ in range(length))
print("Your Generated Password is:", password)