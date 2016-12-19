
with open('input.txt', 'r') as f:
    lines = [line.split(' ') for line in f]
    
    discs = []
    for line in lines:
        discs.append([int(line[3]), int(line[11][0])])
    
    # part 2
    discs.append([11, 0])
    
    i = 0
    while(True):
        valid = True
        for j in range(len(discs)):
            if (((i + j + 1) + discs[j][1]) % discs[j][0]) != 0:
                valid = False
                break
    
        if valid:
            print(i)
            break
        i += 1
