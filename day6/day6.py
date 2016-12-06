import collections

with open('input.txt','r') as f:
    lines = [(lambda line: line.strip())(line) for line in f]
    count = len(lines[0])
    
    for i in range(count):
        #print(collections.Counter(''.join([(lambda line: line[i])(line) for line in lines])).most_common()[0][0], end = '')
        print(collections.Counter(''.join([(lambda line: line[i])(line) for line in lines])).most_common()[-1][0], end = '')
        