
with open('input.txt','r') as f:
    
    lines = [line for line in f]

    positions = {}
    for j in range(8):
        for i in range(len(lines)):
            if str(j) in lines[i]:
                positions[j] = [i, lines[i].index(str(j))]

    
    def getdistance(start):
        nodes = [[start[0], start[1], 0]]
        dict = {}
        while nodes:
            node = nodes.pop(0)
            
            if str(node[0]) + '-' + str(node[1]) not in dict or node[2] < dict[str(node[0]) + '-' + str(node[1])]:
                dict[str(node[0]) + '-' + str(node[1])] = node[2]
            else:
                continue
            
            if node[1] != 0 and lines[node[0]][node[1]-1] != '#':
                nodes.append([node[0], node[1] - 1, node[2] + 1])
            if node[1] != len(lines[0]) - 1 and lines[node[0]][node[1] + 1] != '#':
                nodes.append([node[0], node[1] + 1, node[2] + 1])
            if node[0] != 0 and lines[node[0] - 1][node[1]] != '#':
                nodes.append([node[0] - 1, node[1], node[2] + 1])
            if node[0] != len(lines) - 1 and lines[node[0] + 1][node[1]] != '#':
                nodes.append([node[0] + 1, node[1], node[2] + 1])

        return dict

    distances = {}
    for pos in positions:
        dists = getdistance(positions[pos])
        for pos1 in positions:
            if pos != pos1:
                distances[str(pos) + '-' + str(pos1)] = dists[str(positions[pos1][0]) + '-' + str(positions[pos1][1])]
                
    import itertools
    mindist = -1
    for i in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 0]):
        if i[0] != 0 or i[-1] != 0:
            continue
        dist = 0
        for j in range(len(i) - 1):
            dist += distances[str(i[j]) + '-' + str(i[j+1])]
        if mindist == -1:
            mindist = dist
        else:
            mindist = min(mindist, dist)
    print(mindist)