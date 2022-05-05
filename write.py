# with open("./about.txt","w")as file:
#     file.write("I'm PHT.")
#     file.write("\nI'm 21 years old.")


# #otherwork

# with open("./about.txt","a")as file:
#     file.write("\nI'm a student.")

list=["I'm pht.","\nI'm 21 years old."]

with open("./about.txt","a")as file:
    file.writelines(list)
