file = open("codingal.txt", "r")
counter = 0
content = file.read()
colist = content.split("\n")

for i in colist:
    if 1:
        counter += 1

print("this is te number of lines in the file: ", counter)

