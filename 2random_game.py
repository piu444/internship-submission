import random

print(" Welcome to the Random Number Guessing Game!")

# Random number between 1 and 100
secret_number = random.randint(1, 100)

for i in range(10):  # Player gets 10 attempts
    guess = int(input("Enter your guess (1-100): "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f" Congratulations! You guessed it right in {i+1} attempts.")
        break
else:
    print(f" Sorry! You've used all attempts. The number was {secret_number}.")

   

     
