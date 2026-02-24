
N = int(input("Введите количество чисел в диапозоне (1 ≤ N ≤ 100000) :"))
M = input("Введите через пробел N чисел, каждое из которых по модулю не превышает 2*10e9: ")
set_ = set()
if len(M.split()) <= N:
    for i in M.split():
        set_.add(int(i))
else:
    print("Ошибка. Превышен лимит!")
print(set_)