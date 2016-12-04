
# North
facing = [0,1]
x = 0
y = 0

visited = {}

with open('input.txt', 'r') as f:
    moves = [(lambda dir : [dir[0], int(dir[1:])])(dir) for dir in f.readline().replace(' ', '').split(',')]
    
    found = False
    
