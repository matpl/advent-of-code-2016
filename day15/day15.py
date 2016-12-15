
with open('input.txt', 'r') as f:
    lines = [line.split(' ') for line in f]
    
    stuff = []
    for line in lines:
        stuff.append([int(line[3]), int(line[11][0])])
    
    # part 2
    stuff.append([11, 0])
    
    i = 0
    while(True):
        valid = True
        for j in range(len(stuff)):
            if (((i + j + 1) + stuff[j][1]) % stuff[j][0]) != 0:
                valid = False
                break
    
        if valid:
            print(i)
            break
        i+=1
