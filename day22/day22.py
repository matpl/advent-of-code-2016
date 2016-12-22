
with open('input.txt','r') as f:
    cpt = 0
    grid = []
    lines = [' '.join(line.split()).split(' ') for line in f]
    pos = [0,0]
    for i in range(2, len(lines)):
        first = lines[i][0].split('-')
        x = int(first[1][1:])
        y = int(first[2][1:])
        
        if y >= len(grid):
            grid.append([])
        
        aused = int(lines[i][2][0:-1])
        
        if aused > 200:
            grid[y].append('#')
        elif aused < 15:
            grid[y].append('_')
            pos = [x,y]
        else:
            grid[y].append('.')
        
        for j in range(2, len(lines)):
            if i != j:
                if aused != 0:
                    bavail = int(lines[j][3][0:-1])
                    if aused <= bavail:
                        cpt += 1
    print(str(cpt) + '\n')
        
    # part 2 -> print the grid and solve it by hand... took way too much time to figure this out
    #for line in grid:
    #    print(' '.join(line))

    # general solution
    def getdistance(start, to):
        nodes = [[start[0], start[1], 0]]
        dict = {}
        while nodes:
            node = nodes.pop(0)
            
            if str(node[0]) + '-' + str(node[1]) not in dict or node[2] < dict[str(node[0]) + '-' + str(node[1])]:
                dict[str(node[0]) + '-' + str(node[1])] = node[2]
            else:
                continue
            
            if node[0] != 0 and grid[node[1]][node[0]-1] == '.':
                nodes.append([node[0] - 1, node[1], node[2] + 1])
            if node[0] != len(grid[0]) - 1 and grid[node[1]][node[0] + 1] == '.':
                nodes.append([node[0] + 1, node[1], node[2] + 1])
            if node[1] != 0 and grid[node[1] - 1][node[0]] == '.':
                nodes.append([node[0], node[1] - 1, node[2] + 1])
            if node[1] != len(grid) - 1 and grid[node[1] + 1][node[0]] == '.':
                nodes.append([node[0], node[1] + 1, node[2] + 1])
        return dict[str(to[0]) + '-' + str(to[1])]

    print('\n' + str(getdistance([pos[0],pos[1]], [len(grid[0])-1, 0]) + getdistance([len(grid[0])-2, 0], [0,0])*5))