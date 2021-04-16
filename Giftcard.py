giftcard = 50
print("Giftcard balance: ${}".format(giftcard))
decision = input("Do you wish to purchase skins and weapons for your game?")
if decision == "Yes":
    giftcard -= 35
    print("You have purchased skins and weapons")
    print("Your new balance is: ${}".format(giftcard))
elif decision == "No":
    print("Your giftcard balance remains at ${}".format(giftcard))
else:
    print("Thats not an answer...")
