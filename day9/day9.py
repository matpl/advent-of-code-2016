import re

pattern = re.compile(r'\([0-9]+x[0-9]+\)')
def uncompress(input, i):
    matches = list(re.finditer(pattern, input))
    if len(matches) == 0:
        return len(input)
    else:
        currentpos = 0
        count = 0
        for m in matches:
            no = [int(num) for num in m.group()[1:len(m.group())-1].split('x')]
            if m.start() >= currentpos:
                count += m.start() - currentpos
                currentpos = m.end() + no[0]
                count += no[1] * uncompress(input[m.end():m.end() + no[0]], i+1)
        if currentpos < len(input):
            count += len(input[currentpos:])
        return count

with open('input.txt', 'r') as f:
    text = ''.join([line.strip().replace(' ','') for line in f])
    print(uncompress(text,0))
