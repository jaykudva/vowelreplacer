fileName = "script.txt"
file = open(fileName, "r")
data = file.readlines()
fileToWrite = open("write.txt", "w")


for word in data:
    fileToWrite.write(word.replace("a", "x").replace("e", "x").replace("i", "x").replace("o", "x").replace("u", "x"))
