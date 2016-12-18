rows = 400000

with open('input.txt','r') as f:
    grid = [[]]
    line = f.readline()
    grid[0].append(True)
    for c in line:
        if c == '.':
            grid[0].append(True)
        else:
            grid[0].append(False)
    grid[0].append(True)
    
    for i in range(rows - 1):
        grid.append([True])
        for j in range(1, len(line) + 1):
            l = grid[i][j-1]
            r = grid[i][j+1]
            c = grid[i][j]
                
            if not l and not c and r or not c and not r and l or not l and c and r or not r and c and l:
                grid[i+1].append(False)
            else:
                grid[i+1].append(True)
        grid[i+1].append(True)
        
    cpt = 0
    for i in range(rows):
        for j in range(len(grid[i])):
            if grid[i][j]:
                cpt += 1
                
    print(cpt - len(grid)*2)
