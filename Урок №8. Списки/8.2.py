

N = int(input("Введите число, которое 1 <= N <= 100000: "))
mass = []
if N >= 1 and N <= 100000:
     for i in range(N):
          element = int(input("Введите число, которое 1 <= Ai <= 10e9 :"))
          mass.append(element)
else:
     print("Ошибка!")
mass = [mass[-1]] + mass[:-1]
print(mass)

