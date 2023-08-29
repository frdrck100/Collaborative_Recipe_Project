#we are creating a guessing game

#give the computer a number

#variables can change, can hold values
secret_number = 7
#strings = texts
#integers = numbers
print("Welcome to guess a number!")
print("I am thinking of a number between 0 and 10")

#geeting user input
user_guess = input("make a guess: ")
#user input is always a string

print("you selected: " + user_guess)
user_guess = int(user_guess)


#comparison between user and computer
#if condition then a statement
if secret_number > user_guess:  #comp 7 user 6,5,4,3,2,1
    print("Guess higher")
if secret_number < user_guess:  #comp 7 user 8,9,10
    print("Guess lower")
if secret_number == user_guess:  #comp 7 user 7
    print("Congratulations, you have guessed correctly")
