
num = int(input("Введите число:"))
arry = []
if num >= 1 and num <= 10000:
     for i in range(num):
          a = int(input("Введите число:"))
          if a <= 10e5:
               arry.append(a)
          else:
               print("Ошибка! Число превышает диапозон.")
     arry.reverse()
     print(arry)
else:
     print('Ошибка! Ошибка в записи.')
