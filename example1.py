person={}
while True:
    name=input("enter ur name: ")
    age=input("enter ur age: ")
    person[name]=age
    another = input("another: y/n: ")
    if another == "y":
        continue
    else:
        break
for (key,value) in person.items():
    print(f"{key} is {value} years old.")