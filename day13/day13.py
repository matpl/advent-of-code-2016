grid = []
for y in range(200):
    grid.append([0]*200)
    for x in range(200):
        val = x*x + 3*x + 2*x*y + y + y*y + 1350
        ones = '{0:b}'.format(val).count('1')
        if ones % 2 != 0:
            grid[y][x] = 1

dict = {'1-1': 0}
nodes = [[1,1]]
    
while nodes:
    node = nodes.pop(0)
    
    mov = []
    if node[0] > 0 and grid[node[0]-1][node[1]] == 0:
        mov.append([node[0]-1,node[1]])
    if node[1] > 0 and grid[node[0]][node[1]-1] == 0:
        mov.append([node[0],node[1]-1])
    if node[0] < len(grid)-1 and grid[node[0]+1][node[1]] == 0:
        mov.append([node[0]+1,node[1]])
    if node[1] < len(grid)-1 and grid[node[0]][node[1]+1] == 0:
        mov.append([node[0],node[1]+1])
    
    dist = dict[str(node[0]) + '-' + str(node[1])]
    
    for m in mov:
        k = str(m[0]) + '-' + str(m[1])
        if k not in dict:
            nodes.append(m)
            dict[k] = dist + 1
        elif dist + 1 < dict[k]:
            dict[k] = dist + 1

print(dict['39-31'])
print(sum(dict[item] <= 50 for item in dict))
