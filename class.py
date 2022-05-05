# class Car :
#     def __init__(self, name, wheels) -> None:
#         self.name = name
#         self.wheels = wheels
    
#     def drive(self):
#         print(f"{self.name} is driving.")

# # bmw=Car()
# # print(bmw.name)
# # bmw.drive()

# mercede=Car("mercede", 4)
# print (mercede.wheels)
# mercede.drive()

# class Coffee :
#     def __init__(self, name, choice) -> None:
#         self.name = name
#         self.choice = choice # hot ot cold
    
#     def drive(self):
#         print(f"I want to drink {self.choice} {self.name} coffee.")

# Latte = Coffee("latte", "hot")
# Latte.drive()

class Car:
    steeringwheel = 1

    @classmethod
    def wheel(cls):
        print(f"all cars have only {cls.steeringwheel} wheel.")

print(Car.wheel())