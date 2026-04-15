
from random import randint
matrix_1 = [[randint(-20, 20) for i in range(10)] for l in range(10)]
print("matrix_1")
for i in matrix_1:
    print(i)
print("")
print("matrix_2")
matrix_2 = [[randint(-20, 20) for l in range(10)] for i in range(10)]
for i in matrix_2:
    print(i)

matrix_result = [[0 for i in range(10)] for l in range(10)]


for i in range(len(matrix_1)):
    for j in range(len(matrix_1)):
        matrix_result[i][j] = matrix_1[i][j] + matrix_2[i][j]

for i in range(2):
    print("")
print("matrix_result")

for j in matrix_result:
    print(j)