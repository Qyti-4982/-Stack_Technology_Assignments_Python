
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
def recursion(my_list, i = 0):
    if i < len(my_list):
        print(my_list[i])
        recursion(my_list, i + 1)
    else:
        print("Конец списка!")

recursion(my_list)