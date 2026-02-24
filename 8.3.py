
m = int(input("Введите максимальную массу, которую может перевести одна лодка в диапозоне 1 <= m <= 10e6 (кг) : "))
N = int(input("Введите количество рыбаков в диапозоне 1 <= N <= 100 : "))
mass = []
for i in range(N):
    Ai = int(input("Введите массу каждого рыбака в диапозоне 1 <= Ai <= m: "))
    mass.append(Ai)
mass.sort()
heaviest = len(mass) - 1
easiest_one = 0
boats = 0
while easiest_one <= heaviest:
    if mass[easiest_one] + mass[heaviest] <= m:
        easiest_one += 1
        heaviest -= 1
        boats += 1
    else:
         heaviest -= 1
         boats += 1
print(f'Минимальное количество лодок: {boats}')
