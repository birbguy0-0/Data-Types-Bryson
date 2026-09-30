import random

secret = random.randint(1, 100)
tries = 1
history = []
while True:
    guess = int(input("Type a number (1-100): "))
    if guess > secret:
        print("Lower")
        history.append(guess)
        tries += 1
    elif guess < secret:
        print("Higher")
        history.append(guess)
        tries += 1
    else:
        history.append(guess)
        print(f"You got it in {tries} tries :)") 
        print("History: ")
        print(history)
        break