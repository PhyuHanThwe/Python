# class Restaurant:
#     menus={
#         "pizza" : 5000,
#         "cola" : 1000,
#         'juice' : 1500,
#         "spicy" : 3000
#          }

#     def __init__(self) -> None:
#         self.order=[]
#         self.total=0

#     def table(self,order):
#         self.order.append(order)
#         self.total += self.menu[order]
    
#     def bill():
#         for i in self.order:
#             print(f"{self.order} : {self.menu[order]}")

#         print(f"total price is {self.total}")

# def LL():
#     x = Restaurant()
#     while True:
#         x.table=input("entr ur order: ")
#         another = input("order again? y/n: ")
#         if another == "y":
#             continue
#         else:
#             break
# LL()

class RestaurantTale:
    
    menus={
        "pizza" : 5000,
        "cola" : 1000,
        "juice" : 2000,
        "fired potato" : 1500
    }
    def __init__(self) -> None:
        self.order=[]
        self.total=0

    def addorder(self,i):
        self.order.append(i)
        self.total+=self.menus[i]

    def bill(self):
        for i in self.order:
            print(f"{i} : {self.menus[i]}")

        print(f"total price is {self.total}")
def Startprogram():
    table = RestaurantTale()

    while True:
        i = input("order: ")
        table.addorder(i)
        another = input("order again? y/n: ")
        if another == "y":
            continue
        else:
            table.bill() # ***
            break

Startprogram()