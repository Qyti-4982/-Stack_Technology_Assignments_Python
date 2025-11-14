
a = int(input("Введите пятизначное целое число:"))
un = a % 10
dec= (a % 100 - un) / 10
hund= (a % 1000 - a % 100) / 100
thous = (a % 10000 - a % 1000) / 1000
tenTh= (a % 100000 - a % 10000) / 10000
expr = (dec ** un) * hund  / (tenTh - thous)
print(expr)
