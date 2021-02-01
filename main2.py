#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

import random
number = random.randrange(1,20)
guess = input("I am thinking of a number between 1 - 20. What number do you think it is? ")
guess = int(guess)
if guess == number:
    print("You were actually able to guess it correctly??? Fine... I bet you can't do it again.")
else:
     print("Sorry, but you are incorrect. Better luck next time.")
     print("The number I was thinking of was " + str(number))