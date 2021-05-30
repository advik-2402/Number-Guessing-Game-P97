import random

number = random.randint(1, 9)
chances = 0

print("Guess a number between 1 and 9!")
print("5 chances only!")

while chances < 6:
    guess = int(input("Enter your guess: "))

    if (guess == number):
        print("CONGRATULATIONS! You won!")
    elif (guess > number):
        print("Your guess is too high! Enter a smaller number.")
    else:
        print("Your guess is too low! Enter a bigger number.")

    chances += 1

if (chances == 6):
    print("Hardluck! The number was: ", number)

