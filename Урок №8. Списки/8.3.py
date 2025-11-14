from random import randint as rand
m = int(input("Введите предел массы для одной лодки:"))
n = int(input("Введите количество рыбаков:"))
arry = [rand(1, m) for i in range(n)]
arry.sort()
left = 0
right = n - 1
boats = 0

while(left <= right):
    if left < right and arry[left] + arry[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    boats += 1

print(boats)
