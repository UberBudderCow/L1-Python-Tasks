pin1 = int(input("Enter the first number of your pin"))
pin2 = int(input("Enter the second number of your pin"))
pin3 = int(input("Enter the third number of your pin"))
pin4 = int(input("Enter the fourth number of your pin"))

secret_pin = [pin1, pin2, pin3, pin4]
print(secret_pin)
num1 = 0
num2 = 0
num3 = 0
num4 = 0

pin_finder = [num1, num2, num3, num4]

while pin_finder != secret_pin:
    pin_finder = [num1, num2, num3, num4]
    print(pin_finder)
    if num4 == 9:
        if num3 == 9:
            if num2 == 9:
                num1 += 1
                num2 = 0
                num3 = 0
                num4 = 0
            else:
                num2 += 1
                num3 = 0
                num4 = 0
        else:
            num3 += 1
            num4 = 0
    else:
        num4 += 1
