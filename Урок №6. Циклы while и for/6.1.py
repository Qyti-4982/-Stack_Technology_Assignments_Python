
numbers = int(input("Введите число: "))
count = 0
i = 1
while(i <= numbers):
    a = int(input("Введите число:"))
    if a == 0:
        count += 1
    i += 1
print("Количество нулей: ", count)