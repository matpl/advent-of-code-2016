
# North
facing = [0,1]
x = 0
y = 0

visited = {}

with open('input.txt', 'r') as f:
    moves = [(lambda dir : [dir[0], int(dir[1:])])(dir) for dir in f.readline().replace(' ', '').split(',')]
    
    found = False
    
    for move in moves:
        # rotate direction vector
        if move[0] == 'R':
            facing = [facing[1]*-1, facing[0]]
        else:
            facing = [facing[1], facing[0]*-1]
        
        for i in range(move[1]):
            x += facing[0]
            y += facing[1]
            
            if not found and x in visited:
                if y in visited[x]:
                    print(abs(x) + abs(y))
                    found = True
                else:
                    visited[x].append(y)
            else:
                visited[x] = [y];
    
    print(abs(x) + abs(y))
    