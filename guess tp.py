import random

def guess_number():
    rand_number = random.randint(1, 20)
    list_of_guesses=[]
    while True:
        guess = int(input("Guess an integer between 1 and 20: "))
        list_of_guesses.append(guess)
        if guess > rand_number:
            print("The guess is too high!")
        elif guess < rand_number:
            print("The guess is too low!")
        else:
            print("You got it!")
            break

        print("You guessed the following numbers: ", list_of_guesses)
guess_number()