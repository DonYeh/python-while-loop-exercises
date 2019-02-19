import time

user_input = int(input("Choose a number to start counting from: "))

while user_input >= 0:
    if user_input > 20:
        print("Number too large!")
        user_input = int(
            input("Choose a number SMALLER than 20 to start counting from: "))
        continue
    else:
        print(user_input)
        time.sleep(1)
        user_input -= 1
else:
    print("the end")
