
import collections
pets = {
    1:{"Мухтар": {
        "Вид питомца": "Собака",
        "Возраст питомца": 9,
        "Имя владельца": "Павел"
            },
        },
    2:{
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    }
}

def create():
    if pets:
        last = int(collections.deque(pets, maxlen=1)[0])
        last += 1
    else:
        last = 1
    pet_name = input( 'Имя питомца: ')
    species = input('Вид питомца: ')
    age = int(input('Возраст питомца: '))
    owner = input('Имя владельца: ')

    pets[last] = {pet_name : {
        "Вид питомца" : species,
        "Возраст питомца" : age,
        "Имя владельца" : owner
    }}
        


def read(ID):
    if ID in pets.keys():
        pet_data = pets[ID]
        pet_name = list(pet_data.keys())[0]
        pet_species = pet_data[pet_name]["Вид питомца"]
        age = pet_data[pet_name]["Возраст питомца"]
        name_owner = pet_data[pet_name]["Имя владельца"]
        def get_suffix(age):
            if 10 <= age%100 <= 20:
                return "лет"
            elif age%10 == 1:
                return "год"
            elif 2 <= age%10 <= 4:
                return "года"
            else:
                return "лет"
        print (f'Это {pet_species} по кличке {pet_name}. Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {name_owner}.')
    else: print (False)


    

def update(ID):
    if ID in pets.keys():
        pet_data = pets[ID]
        pet_name = list(pet_data.keys())[0]
        new_name = input("Введите новое имя: ")
        pet_data[new_name] = pet_data.pop(pet_name)
        pet_data[new_name]['Вид питомца'] = input("Введите вид питомца: ")
        pet_data[new_name]['Возраст питомца'] = input("Введите возраст питомца: ")
        pet_data[new_name]['Имя владельца'] = input("Введите имя владельца: ")
    else:
        print(False)
    

def delete(a):
    if ID in pets.keys():
        del pets[a]
    else: print(False)

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def pets_list():
    for pet_id, pet_data in pets.items():
        pet_name = list(pet_data.keys())[0]
        info = pet_data[pet_name]
        print(f"ID: {pet_id}")
        print(f"Имя питомца: {pet_name}")
        print(f"Вид питомца: {info["Вид питомца"]}")
        print(f"Возраст питомца: {info["Возраст питомца"]}")
        print(f"Имя владельца: {info["Имя владельца"]}")
        print("-"*20)


command = input("Введите команду из списка(Добавить(добавление питомца), Изменить(изменение данных о питомце), Прочитать(получить данные о питомце), Удалить(удалить данные о питомце), Проверить(проверка на наличии данных о питомцах), Посмотреть(просмотр данных обо всех питомцах) ),stop(прекращение выполнения программы): ")
    
while command != "stop":
    if command == "Добавить":
        create()
    elif command == "Изменить":
        ID = int(input("Введите индефикатор питомца: "))
        update(ID)
    elif command == "Прочитать":
        ID = int(input("Введите индефикатор питомца: "))
        read(ID)
    elif command == "Удалить":
        ID = int(input("Введите индефикатор питомца: "))
        delete(ID)
    elif command == "Проверить":
        ID = int(input("Введите индефикатор питомца: "))
        print(get_pet(ID))
    elif command == "Посмотреть":
        pets_list()
    else:
        print("Команды нет в списке!")
    command = input("Введите команду из списка(Добавить(добавление питомца), Изменить(изменение данных о питомце), Прочитать(получить данные о питомце), Удалить(удалить данные о питомце), Проверить(проверка на наличии данных о питомцах), Посмотреть(просмотр данных обо всех питомцах) ),stop(прекращение выполнения программы): ")



