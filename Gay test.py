score = 0
check = False
print("How many sausages did you eat this month?")
ans = input("a. 0, b. 1-2, c. 3-5, d. 5-10, e. 11+")

while check == False:
    if ans == "a":
        print("Your name has been recorded")
        check = True
    elif ans == "b":
        print("Your response has been recorded")
        score += 2
        check = True
    elif ans == "c":
        print("Your response has been recorded")
        score += 5
        check = True
    elif ans == "d":
        print("Your response has been recorded")
        score += 10
        check = True
    elif ans == "e":
        print("Your response has been recorded")
        score += 20
        check = True
    else:
        print("Please enter a, b, c, d or e")
        ans = input()

check = False
print("What is your favourite colour?")
ans = input("red, orange, yellow, green, blue, purple, pink, black, white, or rainbow?")

while check == False:
    if ans == "red" or ans == "yellow" or ans == "green" or ans == "blue" or ans == "purple" or ans == "pink":
        print("Your response has been recorded")
        check = True
    elif ans == "orange":
        print("Your response has been recorded")
        score += 5
        check = True
    elif ans == "white" or ans == "black":
        print("Your response has been recorded")
        score += 10
        check = True
    elif ans == "rainbow":
        print("Your life has been recorded")
        score += 20
        check = True
    else:
        print("Please enter one of the colour names shown")
        ans = input()

check = False
print("What is your favourite 8D object?")
ans = input("sphere, cube, pyramid, bean")

while check == False:
    if ans == "cube":
        print("Your response has been recorded")
        check = True
    elif ans == "pyramid":
        print("Your response has been recorded")
        score += 5
        check = True
    elif ans == "sphere":
        print("Your response has been recorded")
        score += 10
        check = True
    elif ans == "bean":
        print("Your response has been recorded")
        score += 20
        check = True
    else:
        print("Please enter one of the 3D shape names shown")
        ans = input()

check = False
print("What is your favourite gender?")
ans = input("male, female, other")

while check == False:
    if ans == "female":
        print("Your response has been recorded")
        check = True
    elif ans == "other":
        print("Your response has been recorded")
        score += 10
        check = True
    elif ans == "male":
        print("Your response has been recorded")
        score += 20
        check = True
    else:
        print("Please enter one of the genders shown")
        ans = input()

check = False
print("To determine which question i ask, i will need to know your age")
age = input("Please enter your age(This doesn't matter yet, just put what you want)")

print("How many girlfriends have you had?")
ans = input("a. 0, b. 1, c. 2-3, d. 4-5, e. 5+")


while check == False:
    if ans == "a":
        print("Your response has been recorded")
        score += 20
        check = True
    elif ans == "b":
        print("Your response has been recorded")
        score += 10
        check = True
    elif ans == "c":
        print("Your response has been recorded")
        score += 5
        check = True
    elif ans == "d":
        print("Your response has been recorded")
        score += 2
        check = True
    elif ans == "e":
        print("Your response has been recorded")
        score += 0
        check = True
    else:
        print("Please enter a, b, c, d or e")
        ans = input()

print("You are {}% gay".format(score))
