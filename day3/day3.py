
import re

sum = 0 + 1 + 2

def validtriangle(sides):
    for i in range(3):
        for j in range(i + 1, 3):
            if i != j and int(sides[i]) + int(sides[j]) <= int(sides[sum - i - j]):
                return 0
    return 1

valid = 0

#with open('input.txt', 'r') as f:
#    for line in f:
#        sides = re.sub(' +',' ', line.strip()).split(' ')
#        valid += validtriangle(sides)

with open('input.txt', 'r') as f:
    while True:
        lines = []
        for i in range(3):
            line = f.readline()
            if not line:
                break
                
            lines.append(re.sub(' +',' ', line.strip()).split(' '))
            
        if len(lines) != 3:
            break
            
        for i in range(3):
            valid += validtriangle([lines[0][i], lines[1][i], lines[2][i]])

print(valid)