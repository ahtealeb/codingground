# Finding Numbers in a Haystack
import re
fhand = open('ActualData.txt')
for line in fhand:
    line = line.rstrip()
    stringlist = re.findall('[0-9]+', line)
print(stringlist)