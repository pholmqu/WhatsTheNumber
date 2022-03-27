from math import *
# import this module for random function
from random import *
# import functions from other file
from hint import hint
from WantToPlay import WantToPlay
from GetMaxMin import GetMaxMin

def main():

    play = WantToPlay()
    
    while play == "yes":
        # setting default values for while loops 
        guess = -1
        plusminus = "+/-"

        # count number of guesses
        count = 0

        min, max = GetMaxMin()

        # random does random float from [0,1), randint does random int from [min,max]
        number = randint(min, max)

        # while loop that checks each time if guess is equal to number
        while guess != number:
            # gets user input for guess
            try:
                guess = int(input("\nGuess a number from " + str(min) + " to " + str(max) + ": "))
            except ValueError:
                print("Please input a number between " + str(min) + " and " + str(max))
            count += 1
            # checks if user guessed correctly
            if guess == number:
                print("\nCongratulations! You guessed the number correctly!")
                print("It took you " + str(count) + " guesses to get the right answer!\n")
                play = WantToPlay()
            else:
                # gets the absolute value of the difference between the guess and the actual number
                diff = abs(number - guess)

                range = max - min
                message = hint(range, diff)
                if number > guess:
                    plusminus = " +"
                elif number < guess:
                    plusminus = " -"

                print(message + plusminus)
                # printing Number, Guess, and Diff for troubleshootin purposes
                # print("Number: " + str(number) + " - Guess: " + str(guess) + " Diff: " + str(diff))

    print("Come again!\n")

main()
