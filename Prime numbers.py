num = int(input("Check for a prime: "))
for i in range(round(num / 2)):
    if i != 0:
        if num % (i+1) == 0:
            print("Not a prime number")
            break
        elif (i+1 == round(num/2)):
            print("{} is a prime number".format(num))

