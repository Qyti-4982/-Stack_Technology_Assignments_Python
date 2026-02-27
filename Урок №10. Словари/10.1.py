
pets = {

  input( "Имя питомца: "):  {

    'Вид питомца': input('Вид питомца: '),

    'Возраст питомца': int(input('Возраст питомца: ')) ,

    'Имя владельца': input('Имя владельца: ')
  }

}

def get_year_form(age):
    if 10 <= age%100 <= 20:
        return "лет"
    elif age%10 == 1:
        return "год"
    elif 2 <= age%10 <= 4:
        return "года"
    else:
        return "лет"
    

for key1, value1 in pets.items():
    keys = list(value1.keys())
    value = list(value1.values())
    print(f"Это {value[0]} по кличке {key1}. {keys[1]}:{value[1]} {get_year_form(value[1])}. {keys[2]}:{value[2]}.")
    
        
