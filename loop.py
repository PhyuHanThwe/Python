# # names = ["ag ag", "kyaw", "phyu", "su"]
# # for name in names:
# #     if name == "phyu":
# #         print(f"{name} is a billionaire.")
# #     else:
# #         print(f"{name} is a worker.")


# # fruits = ["apple", "orange", "watermelon"]
# # for fruit in fruits :
# #     # print("{} is a fruit." .format("fruit"))
# #     print(f"{fruit} is a fruit.")

# flowers = ["rose", "sunflower"]
# for flower in flowers:
#     print(flower)

# x = 10
# x %= 3
# print(x)

# num=10
# count=0
# while count<=num:
#     if (count%2)==0:
#         pass
#     else:
#         print(count)
#     count+=1

# num=11
# count=6
# while count<=num:
#     if (count%3)==0:
#         pass
#     else:
#         print(count)
#     count+=1

# num=15
# count=4
# while count<=num:
#     if (count%5)==0:
#         pass
#     else:
#         print(count)
#     count+=3

num=0
sum=0
count=0
while num>=0:
    num=int(input("num: "))
    if num>=0:
        count+=1
        sum=sum+num 
adv=sum/count  
print("total num:", sum, "adverage:", adv)