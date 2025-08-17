new_file = open('new_file.txt', 'x')
new_file.close()

import os 
print("checking if the file exists or not......")
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")

else:
    print("file does not exist")

my_file = open('codingal.txt', 'w')
my_file.write("hi! i am pengiun and i am 1 yr old")
my_file.close()

os.remove('codingal.txt')
os.rmdir('folder')
