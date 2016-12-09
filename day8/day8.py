rows = 6
cols = 50
grid = [[0 for x in range(cols)] for y in range(rows)]

with open('input.txt','r') as f:
    for line in f:
        if 'rect' in line:
            rect = line[5:].strip().split('x')
            for i in range(int(rect[1])):
                for j in range(int(rect[0])):
                    grid[i][j] = 1
        else:
            if 'rotate row' in line:
                row = [int(i) for i in line[13:].split(' by ')]
            else:
                row = [int(i) for i in line[16:].split(' by ')]
                grid = [list(a) for a in zip(*grid)]
                
            grid[row[0]] = grid[row[0]][-1 * row[1]:] + grid[row[0]][:-1 * row[1]]
            
            if 'rotate column' in line:
                grid = [list(a) for a in zip(*grid)]

print(sum([list.count(1) for list in grid]))
for i in range(10):
    print()
    for j in range(rows):
        print(grid[j][i * 5:(i * 5) + 5])
