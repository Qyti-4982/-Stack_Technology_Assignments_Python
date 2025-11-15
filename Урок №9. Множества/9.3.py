
from random import randint as rand
N = int(input("Введите число:"))
arry = []
for i in range(N):
    arry.append(rand(1, 100000))
c = set(arry)

for j in arry:
    if arry.count(j) >= 2:
        print("Yes")
    else:
        print("No")
