file = open("test.txt", "r")
print(file.name)
print(file.mode) #Tells whether the file is used of reading or writing or both
print(file.readline(), end="")


file.close()