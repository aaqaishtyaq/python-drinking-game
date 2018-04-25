import random
import sys

def show_rules():
    print("""
RULES OF THE GAME

If you guess the number correctly drink for every guess you used
and pass out a drink for each remaining guess you have left.

Guess the number on first try, everyone but you drinks 2x your max guesses.

Guess the number correctly and it's a 3 or 7 reverse the order
of dinks consumed and passed out.

Type:
    'help' to show these
    'quit' to exit game
    'restart' to restart
""")

show_rules()

def game():
    # generate a random num between 1 and 10
    secret_num = random.randint(1, 10)

    # reversed if number is special number ( 3 or 7 )
    reverse_flag = (True if secret_num == 3 or secret_num == 7 else False )

    max_guesses = 3
    guess_count = 0
    while guess_count < max_guesses:
        remaining_guesses = max_guesses - guess_count

        # pluralize output message
        pluralization = ("" if max_guesses - guess_count == 1 else "es")

        try:
            # get a number guess from player
            guess = input("{} remaining guess{}. Guess a number between 1 and 10: ".format(remaining_guesses, pluralization))
            guess = int(guess)
            if guess < 1 or guess > 10: raise Exception
        except ValueError:
            if guess.lower() == "help":
                show_rules()
            elif guess.lower() == "quit":
                sys.exit("Bye!")
            elif guess.lower() == 'restart':
                game()
            else:
                print("{} isn't a number!".format(guess))
        except Exception:
            print('Number out of range')
        else:
            # correct guess
            if guess == secret_num:
                # on first try
                if guess_count == 0:
                    if reverse_flag:
                        print("First try! But the number was {} so you have to take {} drink(s)".format(secret_num, max_guesses * 2))
                        break
                    else:
                        print("First try! Everyone takes {}".format(max_guesses * 2))
                        break
                # after first try
                else:
                    if reverse_flag:
                        print("Reverse, reverse! Take {} and pass out {} drink(s)".format(remaining_guesses, guess_count))
                        break
                    else:
                        print("You got it! Take {} drink(s) and pass out {}".format(guess_count, remaining_guesses))
                        break

            # incorrect guess
            else:
                guess_count += 1
                if guess_count == max_guesses:
                    print("You lose. The number was {}. Drink {} sips".format(secret_num, max_guesses))
                    break
                else:
                    if guess > secret_num:
                        print("Miss, guess lower!")
                    elif guess < secret_num:
                        print("Miss, guess higher!")


    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()
