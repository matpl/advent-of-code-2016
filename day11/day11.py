dict = {}
#solution = '33333333333'
#state = '00121212120'
solution = '333333333333333'
state = '001212121200000'

def isvalidlevel(current, level):
    g = current[:len(current) - 1:2]
    if all(c != level for c in g):
        return True    
    m = current[1::2]
    if all(c != level for c in m):
        return True
    
    for i in range(int((len(state) - 1) / 2)):
        if current[i*2 + 1] == level and current[i*2] != level:
            return False
    return True
    
def isvalidelevator(i, j):
    if i % 2 == j % 2:
        return True
    if j != i + 1:
        return False
    return True

def getmodifiedstate(current, i, j, inc):
    if j != -1:
        return current[:i] + str(int(current[i])+inc) + current[i+1:j] + str(int(current[j])+inc) + current[j+1:len(current)-1] + str(int(current[-1])+inc)
    else:
        return current[:i] + str(int(current[i])+inc) + current[i+1:len(current)-1] + str(int(current[-1])+inc)
        
def getpossiblemoves(current):
    g = current[:len(current) - 1:2]
    m = current[1::2]
    level = current[-1]
    valid = []
    for i in range(len(current) - 1):
        if current[i] == level:
            for j in range(i + 1, len(current) - 1):
                if not isvalidelevator(i, j):
                    continue
                if current[j] == level:
                    if level != '0':
                        pos = getmodifiedstate(current, i, j, -1)
                        if isvalidlevel(pos, level) and isvalidlevel(pos, str(int(level) - 1)):
                            valid.append(pos)
                    if level != '3':
                        pos = getmodifiedstate(current, i, j, 1)
                        if isvalidlevel(pos, level) and isvalidlevel(pos, str(int(level) + 1)):
                            valid.append(pos)
            if level != '0':
                pos = getmodifiedstate(current, i, -1, -1)
                if isvalidlevel(pos, level) and isvalidlevel(pos, str(int(level) - 1)):
                    valid.append(pos)
            if level != '3':
                pos = getmodifiedstate(current, i, -1, 1)
                if isvalidlevel(pos, level) and isvalidlevel(pos, str(int(level) + 1)):
                    valid.append(pos)
    return valid

dict[state] = 0
nodes = [state]
    
while nodes:
    node = nodes.pop(0)
    moves = getpossiblemoves(node)
    dist = dict[node]
    for m in moves:
        if m not in dict:
            nodes.append(m)
            dict[m] = dist + 1
        elif dist + 1 < dict[m]:
            dict[m] = dist + 1

print(dict[solution])
