import random
keep_playing = True

ran_num = random.randint(1, 10)


while True:
    print("random number ",ran_num)
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if ran_num > guess:
        print("Too low!")
    elif ran_num < guess:
        print("Too high!")
    else:
        print("YOU GOT IT!!")
        keep_playing = input("Do you want to keep playing? y/n ")
        if keep_playing == "y":
            ran_num = random.randint(1, 10)
            guess = None


