f = open('inputFile.txt', 'r')
count = 0
for line in f:
    line_split = line.split()
    if line in f:
        line_split = 