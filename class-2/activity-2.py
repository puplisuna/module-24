file_read = open("codingal.txt", "r")
print("file in read mode")
print(file_read.read())
file_read.close()

file_write = open("codingal.txt", "w")
file_write.write("This is a new line added to the file.")
file_write.close()

file_append = open("codingal.txt", "a")
file_append.write("\nfile in append mode.")
file_append.write("\nThis is another line added to the file.")
file_append.close()