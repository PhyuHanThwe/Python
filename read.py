# with open("./text.txt") as file:
#     for line in file:
#         print(line)
# # file.seek(0)
file=open("./text.txt")
file.seek(20)
linelist=file.readlines()
print(linelist)
paga=file.read(60)
print(paga)

print("other")
file.close()

with open("./text.txt") as file:
    for line in file:
        print(line)

print("other")

