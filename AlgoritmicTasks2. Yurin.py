# TASK "Студент"

# class Student:
#     def __init__(self, name="", age=0, average=0, direction=""):
#         self.name = name
#         self.age = age
#         self.average = average
#         self.direction = direction
    
#     def info(self):
#         print(f'''
# Студент: {self.name}
# Возраст: {self.age}
# Средний балл: {self.average}
# Направление: {self.direction}
#         ''')
#     def setName(self, newName):
#         self.name = newName
#         print("Новое имя установлено.")

#     def setAge(self, newAge):
#         self.age = newAge
#         print("Новый возраст установлен.")

#     def setAverage(self, newAverage):
#         self.average = newAverage
#         print("Новый средний балл установлен.")

#     def setDirection(self, newDirection):
#         self.direction = newDirection
#         print("Новое направление установлено.")

# myStudent = Student("Yuri", 18, 80, "1C Programming")
# myStudent.info()
# myStudent.setDirection("Python Programming")
# myStudent.info()    









# TASK "Прямоугольник"

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def perimetr(self):
#         print(f'Периметр этого прямоугольника: {(self.width + self.length) * 2}')
    
#     def area(self):
#         print(f'Плошадь этого прямоугольника: {self.width * self.length}')


# myRectangle = Rectangle(10,6)
# myRectangle.perimetr()
# myRectangle.area()










# TASK "Автомобиль"

# class Auto:
#     def __init__(self, model, manufactureYear, mileage):
#         self.model = model
#         self.manufactureYear = manufactureYear
#         self.mileage = mileage

#     def info(self):
#         print(f'''
# Модель: {self.model}
# Год выпуска: {self.manufactureYear}
# Пробег: {self.mileage}
#         ''')

#     def setModel(self, newModel):
#         self.model = newModel
#         print("Модель изменена.")

#     def setManufactureYear(self, newYear):
#         self.manufactureYear = newYear
#         print("Год выпуска изменен.")

#     def setMileage(self, newMileage):
#         self.mileage = newMileage
#         print("Пробег изменен.")

# myAuto = Auto("Lada", 2007, 1488)
# myAuto.info()

# myAuto.setModel("BMW")
# myAuto.setManufactureYear("2023")
# myAuto.setMileage("1337")

# myAuto.info()










# TASK "Банковский счёт"

# class BankAccount:
#     def __init__(self, client):
#         self.__client = client
#         self.__balance = 0
#         self.__operations = []

#     def replenishment(self, sum):
#         self.__balance += sum
#         self.__operations.append(f'Пополнение на сумму {sum}')
#         print("Операция выполнена.")
    
#     def withdrawal(self, sum):
#         self.__balance -= sum
#         self.__operations.append(f"Снятие со счёта {sum}")
#         print("Операция выполнена.")

#     def info(self):
#         print("========================")
#         print(f'Клиент: {self.__client}\nБаланс: {self.__balance}')
#         if len(self.__operations) == 0:
#             print("Операции со счётом не производились.")
#         else:
#             print("История операций: ")
#             for i in range(len(self.__operations)):
#                 print(self.__operations[i])
#         print("========================")

# myAccount = BankAccount("Yuri")
# myAccount.info()

# myAccount.replenishment(26500)
# myAccount.withdrawal(95)
# myAccount.withdrawal(160)
# myAccount.withdrawal(450)
# myAccount.replenishment(3000)

# myAccount.info()











# TASK "Треугольник"

# class Triangle:
#     def __init__(self, side_1, side_2, side_3):
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
    
#     def defineType(self):
#         if(self.side_1 == self.side_2 == self.side_3):
#             print("Этот треугольник равносторонний.")
#         elif((self.side_1 == self.side_2) or (self.side_1 == self.side_3) or (self.side_2 == self.side_3)):
#             print("Этот треугольник равнобедренный")
#         else:
#             print("Этот треугольник разносторонний.")
    
#     def area(self):
#         self.semiperimeter = (self.side_1 + self.side_2 + self.side_3) / 2
#         print(f'Площадь этого треугольника: {(self.semiperimeter*(self.semiperimeter - self.side_1) * (self.semiperimeter - self.side_2) * (self.semiperimeter - self.side_3))**0.5}')


# myTriangle = Triangle(5,4,3)
# myTriangle.area()
# myTriangle.defineType()