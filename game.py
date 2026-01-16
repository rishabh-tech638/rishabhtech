import random

print("🎮 Welcome to Guess The Number Game!")
print("I have selected a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too Low ❌")
    elif guess > number:
        print("Too High ❌")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
