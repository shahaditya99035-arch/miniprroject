import random

secret = random.randint(1, 100)
print("mai na ek number choice kar liya ha  1 se 100 thak ka bich mai . Guess karo")

while True:
    guess = int(input("tera guess: "))
    if guess < secret:
        print("kum ha jada number guess karo")
    elif guess > secret:
        print("jada number hoga ha thoda kum karo")
    else:
        print("sahi ha tera guess!")
        break