with open('input.txt','r') as f:
    lines = [map(int, line.split('-')) for line in f]
    lines.sort(key=lambda x: x[0])
    
    high = -1
    cpt = 0
    for line in lines:
        if line[0] > high:
            cpt += line[1] - line[0] + 1
            high = line[1]
        elif line[1] > high:
            cpt += line[1] - high
            high = line[1]

    print(4294967296 - cpt)
    