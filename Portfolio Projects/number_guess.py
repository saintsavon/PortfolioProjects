from random import randint

number = randint(1, 10)
player_name = input("Hello, what's your name? ")
number_of_guess = 0
print("Okay " + player_name + ', I am thinking of a number between 1 and 10:')

while number_of_guess < 5:
    guess = int(input())
    number_of_guess += 1
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break
if guess == number:
    print("You correctly guessed the number in " + str(number_of_guess) + " tries!")
else:
    print("You did not guess the correct number. The correct number was " + str(number))
