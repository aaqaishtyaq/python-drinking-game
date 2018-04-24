import random
import sys

print("""
RULES OF THE GAME

If you guess the number correctly drink for every guess you used
and pass out a drink for each remaining guess you have left

Guess the number on first try, everyone but you drinks 2x your max guesses.

Guess the number correctly and it's a 3 or 7 reverse the order
of dinks consumed and passed out.
""")

# generate a random num between 1 and 10
secret_num = random.randint(1, 10)
reverse_flag = (True if secret_num == 3 or secret_num == 7 else False )

max_guesses = 3
guess_count = 0
while guess_count < max_guesses:
    # pluralize output message
    pluralization = ("" if max_guesses - guess_count == 1 else "es")
    # get a number guess from player
    guess = int(input("{} remaining guess{}. Guess a number between 1 and 10: ".format(max_guesses - guess_count, pluralization)))

    # compare guess to secret number
    if guess == secret_num:
        if guess_count == 0 and reverse_flag:
            sys.exit("First try! But the number was {} so you have to take {} drink(s)".format(secret_num, max_guesses * 2))
        else:
            sys.exit("First try! Everyone takes {}".format(max_guesses * 2))

        if reverse_flag:
            sys.exit("Reverse, reverse! Take {} and pass out {} drink(s)".format(max_guesses - guess_count, guess_count))

    elif guess > secret_num:
        print("Miss, guess lower!")
    elif guess < secret_num:
        print("Miss, guess higher!")

    guess_count += 1

print("You lose. The number was {}. Drink {} sips".format(secret_num, max_guesses))
