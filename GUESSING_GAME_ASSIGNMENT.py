#adding a function add life points
#This function has a counter that increases every time the user gets a guess correctly and
#When the count == 5, increases the user’s curr_point by 10 points and resets the counter.

from time import sleep
import sys
import random


#DECLARE LEADERBOARD
#GUESS A NUMBER GAME THAT LETS US TRACK OUR SCORE AS WE PLAY

#WE NEED USER INPUT
# VARIABLE TO SAVE SCORES
#IMPORT RANDOM
# ONCE THEY QUIT/RESTART WE RESET OUR SCORES
#HINTS IF THEY GUESS WRONG
#HINTS VARIABLE - TRYS = 3

#For Introduction
def print_slow(intro):
    for char in intro:
        print(char,end='')
        sys.stdout.flush()
        sleep(0.05)

#To Potentially save the player on the Leader Board
def ask_player_name():
    while True:
        username = input("What is your name? Please make sure its not more that 8 characters long!:")

        if len(username) > 2 and len(username) < 8:
            return username
        print("INVALID USERNAME: Name should be between 3 to 8 characters")

def get_user_guess():
    while True:
        guess = input("Enter a valid number between 1 - 5: ")
        try:
            guess = int(guess)
            if guess >= 1 and guess <= 5:
                return guess
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 10")

#To get the guess for our game
def generate_random_number():
    number = random.randint(1, 5)
    return number

def get_hint(guess, number, curr_points):
    if guess > number:
        print("Your Guess is too High! Go Lower")
    else:
        print("Your Guess is too Low! Go Higher")

    curr_points -= 5
    print(f"LIFE POINTS - 5 : {curr_points}")
    return curr_points

#check if user guess is correct
#add life points 
def validate_guess(guess, number, curr_score, curr_points, lifepoints_counter):
    while True:
        if guess == number:
            curr_score += 5
            print(f"CORRECT! You earned 5 points")
            lifepoints_counter += 1
            if lifepoints_counter == 5:
                curr_points += 10
                lifepoints_counter = 0
                print ("You've earned 10 extra life points!")
            break
        else:
            try:
                print("Wrong Guess!")
                choice = input("Do you want a hint? YES/Y OR NO/N: ").lower()

                if choice in ('y', 'yes'):
                    if curr_points > 5:
                        curr_points = get_hint(guess, number, curr_points)
                        new_guess = get_user_guess()
                        return validate_guess(new_guess, number, curr_score, curr_points)
                    else:
                        print("YOU DON'T HAVE ENOUGH POINTS")
                        curr_points -=10
                        print(f"LIFE POINTS - 10 : {curr_points}")
                        break
                else:
                    curr_points-=10
                    print(f"LIFE POINTS - 10 : {curr_points}")
                    break
            except ValueError:
                print("INVALID CHOICE")

    return curr_points, curr_score, lifepoints_counter


def play_again():
    while True:
        user_input = input("Would you like to play again? Yes/y or No/n: ").lower()

        if user_input in ("yes", "y"):
            print("GREAT LETS HAVE ANOTHER ROUND")
            return main()
        elif user_input in ("no", "n"):
            print("GOOD BYE ITS SAD TO SEE YOU GO")
            break
        else:
            print("You have to choose between Yes or no ")


introduction =  '''
Hello and Welcome to our Guessing Game.
You initially start with 50 LIFE POINTS.
For Every Wrong Guess -10 LIFE POINTS.
For Every Time You use a HINT - 5 LIFE POINTS.
For Every 5 correct guesses + 5 LIFE POINTS.
You can see your current SCORE and LIFE POINTS after every guess.
You can see your position on our LeaderBoard after playing the game.
GOOD LUCK !
'''

# print_slow(introduction)
# ask_player_name()
# get_user_guess()


LEADERBOARD = {}
LIFEPOINTS = 50

def main():
    curr_score = 0
    curr_points = LIFEPOINTS
    lifepoints_counter = 0
    print_slow(introduction)
    username = ask_player_name().lower()


    while curr_points > 0:
        guess = get_user_guess()
        number = generate_random_number()

        curr_points, curr_score = validate_guess(guess, number,curr_score, curr_points)
        print(f"CURRENT SCORE:{curr_score}, CURRENT LIFE POINTS:{curr_points}")

        if  curr_points <= 0:
            print("GAME OVER")
            if LEADERBOARD.get(username) is None:
                print(f"Your Highest Score Ever is {curr_score}")
                LEADERBOARD[username] = curr_score
            else:
                if curr_score > LEADERBOARD[username]:
                    print("New Highscore! {curr_score}")
                    LEADERBOARD[username] = curr_score

    print("LEADERBOARD")
    for player, score in LEADERBOARD.items():
        print(f"{player}:{score}")

    play_again()

main()