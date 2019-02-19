import random
my_random_number = random.randint(1, 10)
guesses_left = 4

print("I am thinking of a number between 1 and 10.")
guess = int(input("What's the number? "))
while guess != my_random_number and guesses_left > 0:
    if guess > my_random_number:
        print(("%d is too high.") % guess)
        guesses_left -= 1
        guess = int(input("What's the number? "))
        continue
    elif guess < my_random_number:
        print(("%d is too low.") % guess)
        guesses_left -= 1
        guess = int(input("What's the number? "))
        continue
    else:
        print("You got it!")
# elif guess == 1:
#     print("You are out of guesses!")
else:
    print("out of guesses!")
