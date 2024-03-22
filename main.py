import random
keep_playing = True

ran_num = random.randint(1, 10)
guess = None

while guess != ran_num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess:
        if ran_num > guess:
            print("Too low!")
        elif ran_num < guess:
            print("Too high!")
        elif guess == ran_num:
            print("YOU GOT IT!!")
    keep_playing = input("Do you want to keep playing? y/n ")
    if keep_playing == "y":
        guess = None


