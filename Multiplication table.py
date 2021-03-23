num1 = 1
num2 = 1
for i in range(144):
    print("{} x {} = {}".format(num1, num2, num1 * num2))
    if num2 == 12:
        num1 += 1
        num2 = 1
    else:
        num2 += 1
