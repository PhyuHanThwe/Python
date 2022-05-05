# x = [2,3,2,4,8,9,1]
# print(sorted(x))

# y = [20,30,20,50]
# print(set(y))

person = {}
while True:
    name = input("name: ")
    age = input("age: ")
    person[name]=age
    another = input("another y/n: ")
    if another == "y":
        continue
    else:
        break
ages = list(person.values())
for age in set(ages):
    count = age.count(age)
    print(f"{age} years old - {count}")
# 20 years old - 2
# 18 years old - 1