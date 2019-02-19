height = int(input("Height? "))
width = int(input("Width? "))
space = " "


def print_rectangle(height, width):
    row = 0
    while row < height:
        if row == 0 or row == height - 1:
            print(width * "*")
            row += 1
        else:
            print("*" + space*(width-2) + "*")
            row += 1


print_rectangle(height, width)
