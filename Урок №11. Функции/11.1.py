
from math import factorial as fact
a = abs(int(input("Число ")))
def Numb(a):
    return fact(a)
b = []
while(a >= 1):
    b.append(Numb(a))
    a -= 1
print(b)
