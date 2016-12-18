import hashlib

rows = 4
cols = 4
distance = -1
path = ''

input = 'vkjiggvb'

def getdoors(h):
    m = hashlib.md5()
    m.update(h.encode('utf8'))
    h = m.hexdigest()[0:4]
    for i in range(len(h)):
        if ord(h[i]) < 98:
            h = h[0:i] + 'c' + h[i+1:]
        else:
            h = h[0:i] + 'o' + h[i+1:]
    return h
    
moves = [[input, 0, 0, 0]]

while moves:
    m = moves.pop(0)
    
    if m[1] == rows - 1 and m[2] == cols - 1:
        if distance == -1 or m[3] > distance: # m[3] < distance:
            distance = m[3]
            path = m[0]
        continue
            
    #if distance != -1 and m[3] >= distance:
    #    continue

    doors = getdoors(m[0])
    if m[1] > 0 and doors[0] != 'c':
        moves.append([m[0] + 'U', m[1] - 1, m[2], m[3] + 1])
    if m[1] < rows - 1 and doors[1] != 'c':
        moves.append([m[0] + 'D', m[1] + 1, m[2], m[3] + 1])
    if m[2] > 0 and doors[2] != 'c':
        moves.append([m[0] + 'L', m[1], m[2] - 1, m[3] + 1])
    if m[2] < cols - 1 and doors[3] != 'c':
        moves.append([m[0] + 'R', m[1], m[2] + 1, m[3] + 1])

print(distance)
