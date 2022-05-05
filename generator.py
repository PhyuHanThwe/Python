# with open("./text.txt")as file:
#     paragraph=file.read()

#     paraCount=int(input("paragraph count: "))

# with open("./generator.txt","a")as write_file:
#     for count in range(paraCount):
#         write_file.write(paragraph+"\n\n")


# words=["apple," "orange," "lime", "lemon"]
# from random import randint
# def function(word):
#     randomIndex=randint(0,len(words)-1)
#     return f"{words[randomIndex]} {word}"
# with open("./text.txt")as file:
#     paragraph=file.read()
#     wordlist=paragraph.split()
#     setencelist=list(map(function,wordlist))
#     paraCount=int(input("paragraph count: "))

#     for count in range(paraCount):
#         with open("./generator.txt","a")as write_file:
#             write_file.write("".join(setencelist)+"\n\n")

words=["apple", "orange", "lime", "lemon"]
from random import randint
def function(a):
    randomIndex=randint(0,len(words)-1)
    return f"{words[randomIndex]} {a}"
with open("./text.txt")as file:
    paragraph=file.read()
    wordlist=paragraph.split()
    new=list(map(function,wordlist))
    paraCount=int(input("paragraph count: "))

    for count in range(paraCount):
        with open("./generator.txt","a")as write_file:
            write_file.write("".join(new)+"\n\n")

