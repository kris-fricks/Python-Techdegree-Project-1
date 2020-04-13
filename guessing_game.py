"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys


def start_game():
    print("""
--------------------------------------------------
Welcome to The Number Guessing Game, Come on down!
--------------------------------------------------
""")
    
    solution = random.randint(1, 10)
    attempt_count = 0
    high_score = []
    
    while True:
        guess = (input("Pick a number between 1 and 10:  "))
        attempt_count += 1
        
        high_score.append(attempt_count)
        
        try:
            guess = int(guess)
        except ValueError:
            print("We ran into an error. Try again")
        else:
            if guess > 10:
                print("Only pick a number between 1 and 10. Try again.")
            elif guess > solution: 
                print("It's lower")
            elif guess < solution: 
                print("It's higher")
            elif guess == solution:
                print("You got it!")
                print("It took you {} attempts.".format(attempt_count))
                play_again = input("Would you like to play again? (Yes/No)  ")
        
                if play_again.lower() == "yes":
                    print("\nTHE CURRENT HIGH SCORE IS: {}".format(len(high_score)))
                    start_game()
                else:
                    print("Closing game, thanks for playing!")
                    sys.exit()
                    
                          
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    
        
    
    
    
    
    



