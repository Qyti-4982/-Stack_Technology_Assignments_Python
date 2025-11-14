from random import randint as rand
N = int(input("Введите число: "))
if N >= 1 and N <= 10000:
    arry = [rand(1, 10000) for i in range(N)]
print(arry)
arry = [arry[-1]] + arry[:-1]
print(arry)
