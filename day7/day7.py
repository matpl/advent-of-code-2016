import re

def getabba(line, length):
    res = []
    for i in range(len(line) - (length - 1)):
        if(line[i:i+length] == line[i:i+length][::-1] and line[i:i+length] != line[i:i+length][0] * length):
            res.append(line[i:i+length])
    return res

cpt4 = 0
cpt3 = 0
with open('input.txt','r') as f:
    for line in f:
        p = re.compile('\[[a-z]+\]')
        bracket = [item[1:len(item)-1] for item in p.findall(line)]
        for item in bracket:
            line = line.replace('[' + item + ']', ' ')

        if not any(len(getabba(item, 4)) > 0 for item in bracket):
            if len(getabba(line, 4)) > 0:
                cpt4 += 1

        abas = [val for sublist in [getabba(item, 3) for item in bracket] for val in sublist]
        for aba in abas:
            if (aba[1:3] + aba[1]) in line:
                cpt3 += 1
                break

print(cpt4)
print(cpt3)
