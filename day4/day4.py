import collections

valid = 0

with open('input.txt', 'r') as f:
    for line in f:
        checksum = line[line.rfind('[')+1:line.rfind(']')]
        name = line[0:line.rfind('-')].replace('-','')
        id = line[line.rfind('-')+1:line.rfind('[')]

        char_counter = collections.Counter(name)
        chars = sorted(char_counter.most_common(), key=lambda e: (e[1]*-1, e[0]))
        realchecksum = ''.join([item[0] for item in chars[:5]])
        
        if realchecksum == checksum:
            valid += int(id)
            
            realname = ''.join([(lambda letter: chr((ord(letter) - 97 + int(id)) % 26 + 97))(letter) for letter in name])
            if "northpole" in realname:
                print(id)

print valid
