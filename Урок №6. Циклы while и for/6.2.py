
numbers = int(input("Введите число: "))
count = 0
i = 1
a = 1
if numbers > 0 and numbers <= 2e9:
    while(a <= numbers):
        if numbers % a == 0:
            count +=1
        a += 1
print("Количество натуральных делителей:", count)