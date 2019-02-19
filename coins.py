coins = 0
another_coin = True
print("You have %d coins" % coins)
while another_coin:
    want_coins = input("Do you want another? ")
    if want_coins == "yes":
        coins += 1
        print("You have %d coins" % coins)
    else:
        print("byeeeeee")
        another_coin = False
