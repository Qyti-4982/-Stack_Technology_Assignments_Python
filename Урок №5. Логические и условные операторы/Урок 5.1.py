
expr = int(input("Введите число:"))
if expr % 2 == 0:
    if expr == 0:
        print("нулевое число")
    if expr > 0:
        print("положительное чётное число")
    if expr < 0:
        print("отрицательное чётное число")
else:
    print("число не является чётным")
