# def name1(i):
#     def wrapper(name):
#         #before
#         print("hello")
#         i(name)
#         #after
#         print("good bye")
#     return wrapper

# @name1
# def name2(name):
#     # name=input('enter ur name: ')
#     print(name)
# name2(input('enter ur name: '))


class CoffeeShop:
    menu={
        "hot coffee":1500,
        "cold coffee":2000
    }
    def __init__(self) -> None:
        self.order=[]
        self.total=0

    def addorder(self,a):
        self.order.append(a) #a=order
        self.total+=self.menu[a]

    def bill(self):
        for a in self.order:
            print(f"{a}:{self.menu[a]}")
        print(f"Total bill is {self.total}")

def coffee(test):
    def wrapper(n):
        print("What kind of coffee do u want to drink?")
        test(n)
        print("Thanks")
    return wrapper

@coffee
def start(n):
    kk=CoffeeShop()

    while True:
        a=input("order: ")
        kk.addorder(a)
        another=input("order again? y/n: ")
        if another=="y":
            continue
        else:
            kk.bill()
            break
# @coffee
# def start(n):
#     print(n)

start(CoffeeShop())