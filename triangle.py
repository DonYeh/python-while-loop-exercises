user_input = int(input("please enter number of rows: "))
row = 0
while (row < user_input):
    row += 1
    spaces = user_input - row
 
    spaces_counter = 0
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()
