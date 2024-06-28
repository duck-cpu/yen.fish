#import module to generate random numbers

import random

#generating random number and assigning it to variable

randomNumber = random.randrange(1, 100)

#defining the variable for number of guesses

numberOfGuesses = 1

#setting limits for guesses

lowerLimit = 1
upperLimit = 100

#AI to guess the middle number between the lower and upper limit

guess = int((lowerLimit + upperLimit)/2)
print("AI guesses:", guess)

while guess != randomNumber:

    numberOfGuesses += 1

    if guess > randomNumber:
        print(guess, "is too high")
        upperLimit = guess
        guess = int((lowerLimit + upperLimit)/2)
        print("AI guesses:", guess)
    elif guess < randomNumber:
        print(guess, "is too low")
        lowerLimit = guess
        guess = int((lowerLimit + upperLimit)/2)
        print("AI guesses:", guess)
    else:
        print("AI got it!")

print("AI guessed correctly and, it took", numberOfGuesses, "guesses!")
