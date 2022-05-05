from urllib.request import urlretrieve

link=input("download link : ")
filename=input("filename: ")

urlretrieve(link,"image/"+filename+".jpg")