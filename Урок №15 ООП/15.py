# ЗАДАНИЕ 1
class Transport:

   def __init__(self, name, max_speed, mileage):

    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage


class Car(Transport):
  def specifications(self):
    print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

car_1 = Car( "Renaul Logan", 180, 12)
car_1.specifications()

#ЗАДАНИЕ 2

class Transport:

   def __init__(self, name, max_speed, mileage):

    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage
 

   def seating_capacity(self, capacity):

       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
   

class Autobus(Transport):
  def seating_capacity(self, capacity = 50):
    return super().seating_capacity(capacity)
  
autobus = Autobus("Renaul Logan", 180, 12)

print(autobus.seating_capacity())
