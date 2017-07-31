#Guess the number game
import random, os

print("Hello, what is your name ?")
playerName = input()

print("Well, hello "+playerName+". I'm thinking of a number between 1 and 20. Can you guess it ?")
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break #This condition is for the correct guess
if guess == secretNumber:
    if guessesTaken == 1:
        print("Good job, "+playerName+"! You guessed my number in "+str(guessesTaken)+" guess.")
    else:
        print("Good job, "+playerName+"! You guessed my number in "+str(guessesTaken)+" guesses.")
else:
    print("Nope, the number I was thinking of, was: "+str(secretNumber))


os.system("pause")