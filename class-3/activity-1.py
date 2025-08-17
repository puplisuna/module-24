with open ('codingal.txt', 'w') as file:
    file.write("codingal is on a to inspire school kids to fall in love with codingal\n")
    file.close()

with open ('codingal.txt', 'r') as file:
    data = file.readlines()
    print("words in the file are...")
    for line in data:
        words = line.split()
        print(words)
    file.close()    