from random import randint as rand
N = int(input("Введите число:"))
arry = []
for i in range(N):
    arry.append(rand(1, 100000))
    arry.append(" ")
a = len(arry)
b = set(arry)
c = len(b)
g = a - c
print("Разность:", g)
