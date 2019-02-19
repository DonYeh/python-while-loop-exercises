user_input = input("Text? ")
height = 3
width = len(user_input) + 4
space = " "

count = 0


def print_banner(height, width):
    row = 0
    while row < height:
        if row == 0 or row == height - 1:
            print(width * "*")
            row += 1
        else:
            print("* " + user_input + " *")
            row += 1


print_banner(height, width)


# Bonus: Print a Banner
# Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:

# $ python banner.py
# Text? Welcome to DigitalCrafts
# ****************************
# * Welcome to DigitalCrafts *
# ****************************
