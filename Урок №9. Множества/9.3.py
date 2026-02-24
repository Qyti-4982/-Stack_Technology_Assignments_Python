
list_ = map(int,input("Введите через пробел список чисел: ").split())
set_ = set()

for i in list_:
    if i in set_:
        print("Yes")
    else:
        set_.add(i)
        print("No")