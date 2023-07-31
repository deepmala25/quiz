import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"the number are between 1 and {x}: "))
        if guess < random_number :
            print("sorry, try again! too low")
        elif guess > random_number :
            print("sorry , try again! too high")
    print(f"yeah you guess the right number {random_number} correctly!!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low,high)
        feedback = input(f"the number {guess} is high(h) or low(l) or correct(c): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
    print(f"computer guessed the number {guess} correctly!!!")






guess(10)
computer_guess(10)
