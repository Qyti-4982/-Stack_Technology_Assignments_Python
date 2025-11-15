from random import randint as rand
N = int(input("Ввод "))
a = []
b = []
for i in range(N):
    a.append(rand(1, 100000))
    b.append(rand(1, 100000))
c = set(a + b)
print("Одновременно: ", len(c))