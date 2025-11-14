
from random import randint as rand
num = int(input("Введите число:"))
arry = []
if num <= 10e5:
     for i in range(num):
          a = (rand(1, 100000))
          print(a)
          arry.append(a)
for i in reversed(arry):
     print(i)
