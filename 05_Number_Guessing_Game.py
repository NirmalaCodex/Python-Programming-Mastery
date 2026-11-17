number = 27
attempts = 0

print("======= GUESS THE NUMBER =======")

while True:
    guess = int(input("Guess the number: "))

    attempts += 1

    if guess > number:
        print("Too High!")

    elif guess < number:
        print("Too Low!")

    else:
        print("Congratulations!")
        print("You guessed correctly.")
        break

print("Total Attempts: ", attempts)
print("================================")