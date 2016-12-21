from itertools import permutations
from collections import deque

scrambled = 'fbgdceah'
perms = list([ ''.join(p) for p in permutations(scrambled)])

with open('input.txt','r') as f:
    lines = [line.split(' ') for line in f]

for pw in perms:
    unscrambled = pw
    for line in lines:
        chars = list(pw)
        if line[0].strip() == 'swap':
            x = line[2].strip()
            y = line[5].strip()
            if line[1].strip() == 'position':
                chars[int(line[2])], chars[int(line[5])] = chars[int(line[5])], chars[int(line[2])]
            elif line[1].strip() == 'letter':                
                for i in range(len(chars)):
                    if chars[i] == x:
                        chars[i] = y
                    elif chars[i] == y:
                        chars[i] = x
        elif line[0].strip() == 'rotate':
            chars = deque(chars)
            if line[1].strip() == 'right':
                rot = int(line[2])
                chars.rotate(rot)
            elif line[1].strip() == 'left':
                rot = int(line[2])
                chars.rotate(rot * -1)
            else:
                letter = line[6].strip()
                ind = pw.index(letter)
                if ind < 4:
                    chars.rotate(ind + 1)
                else:
                    chars.rotate(ind + 2)
            chars = list(chars)
        elif line[0].strip() == 'reverse':
            rev = pw[int(line[2]):int(line[4])+1][::-1]
            chars[int(line[2]):int(line[4])+1] = rev
        else:
            chars.insert(int(line[5]), chars.pop(int(line[2])))
        pw = ''.join(chars)
    if pw == scrambled:
        print(unscrambled)
        break
