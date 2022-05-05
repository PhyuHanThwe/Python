class BookStore:
    menus={
        "comic book" : 1500,
        "novel" : 3000,
        "Mya Than Tint" : 4500,
        "Jue" : 3000,
        "pi moe ninn" : 1000
    }

    def __init__(self) -> None:
        self.order = []
        self.total = 0

    def addorder(self,i):
        self.order.append(i) # i = menu[key]
        self.total+=self.menus[i]
    
    def bill(self):
        for i in self.order:
            print(f"{i} : {self.menus[i]}")

        print(f"Total price is {self.total}")

def Start():
    counter = BookStore()
    
    while True:
        i = input("enter ur choice: ")
        counter.addorder(i)
        another = input("order again? y/n : ")
        if another == "y":
            continue
        else:
            counter.bill()
            break
Start()