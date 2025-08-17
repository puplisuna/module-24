outputFile = open('updated_file.txt', 'w')
inputFile = open('reapeted_file.txt', 'r')

lines_seen_so_far = set()
print("eliminating dublicate lines...")

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()