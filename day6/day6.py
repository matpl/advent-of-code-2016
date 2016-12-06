import collections

with open('input.txt','r') as f:
    lines = [(lambda line: line.strip())(line) for line in f]
    
    print(''.join(collections.Counter(col).most_common()[0][0] for col in zip(*lines)))
    print(''.join(collections.Counter(col).most_common()[-1][0] for col in zip(*lines)))
