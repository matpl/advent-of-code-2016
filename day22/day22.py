
with open('input.txt','r') as f:
    cpt = 0
    grid = []
    lines = [' '.join(line.split()).split(' ') for line in f]
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
        else:
            grid[y].append('.')
        
        for j in range(2, len(lines)):
            if i != j:
                if aused != 0:
                    bavail = int(lines[j][3][0:-1])
                    if aused <= bavail:
                        cpt += 1
                        
    grid[0][0] = '0'
    print(str(cpt) + '\n')
    
    # part 2 -> print the grid and solve it by hand... took way too much time to figure this out
    for line in grid:
        print(' '.join(line))
