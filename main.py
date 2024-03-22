import random
keep_playing = True

while keep_playing:
    ran_num = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == ran_num:
        want_continue = input("Do you want to keep playing? y/n ")
        if want_continue == "y":
            keep_playing = True
        else:
            keep_playing = False
