
import collections
pets = {}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    pets[input( "Имя питомца ")] = {

        'Вид питомца': input('Вид питомца '),

        'Возраст питомца': int(input('Возраст питомца ')) ,

        'Имя владельца': input('Имя владельца ')
        }
    last += 1
    return pets
a = input("Имя")
def read (a):
    print("Это", pets[a['Вид питомца']], "по кличке",a )

def update():
    pets[a] = input()
    a['Вид питомца'] = input()
    a['Возраст питомца'] = input()
    a['Имя владельца'] = input()

def delete(a):
    del pets[a]
    




