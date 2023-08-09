import random

while True:
    start = input("Enter the start of the range: ")
    try:
        start = int(start)
        break
    except ValueError as e:
        print("Please enter a valid number.")
        continue

while True:
    end = input("Enter the end of the range: ")
    try:
        end = int(end)
        if end >= start:
            break
        else:
            print("Please enter a valid number.")
            continue
    except ValueError as e:
        print("Please enter a valid number.")
        continue

rand_num = random.randint(start,end)
num_attempts = 1

while True:
    try:
        guess = input("Guess a number: ")
        guess = int(guess)
        if guess == rand_num:
            if num_attempts != 1:
                print(f"You guessed the number in {num_attempts} attempts")
            else:
                print(f"You guessed the number in {num_attempts} attempt")
            break
        else:
            num_attempts += 1
            continue
    except ValueError as e:
        print("Please enter a valid number.")
        continue