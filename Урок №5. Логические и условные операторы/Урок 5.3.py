
Mikle = float(input("Вложения Майкла,$:"))
Ivan = float(input("Вложения Ивана,$:"))
doorstep = 100000.00

if Mikle >= doorstep and  Ivan >= doorstep:
    print(2)
elif Mikle >= doorstep and Ivan <= doorstep:
    print("Mike")
elif Mikle <= doorstep and Ivan >= doorstep:
    print("Ivan")
elif (Mikle <= doorstep and Ivan <= doorstep) and (Mikle + Ivan >= doorstep):
    print(1)
elif (Mikle <= doorstep and Ivan <= doorstep) and (Mikle + Ivan <= doorstep):
    print(0)
