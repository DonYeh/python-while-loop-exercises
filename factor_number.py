user_input = int(input("Enter a number: "))
value = 1
print(("factors of a given number %d are: ") % user_input)

while (value <= user_input):
    if (user_input % value == 0):
        print(value)
    value += 1
