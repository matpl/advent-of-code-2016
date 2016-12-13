dict = {'a':0, 'b':0, 'c':1, 'd':0}
with open('input.txt', 'r') as f:
    lines = [line.split(' ') for line in f]
    cpt = 0
    while cpt < len(lines):
        if lines[cpt][0] == 'cpy':
            if lines[cpt][1].strip().isnumeric():
                dict[lines[cpt][2].strip()] = int(lines[cpt][1])
            else:
                dict[lines[cpt][2].strip()] = dict[lines[cpt][1].strip()]
        elif lines[cpt][0] == 'inc':
            dict[lines[cpt][1].strip()] += 1
        elif lines[cpt][0] == 'dec':
            dict[lines[cpt][1].strip()] -= 1
        elif lines[cpt][0] == 'jnz':
            reg = lines[cpt][1].strip()
            if reg.isnumeric() and reg != '0' or not reg.isnumeric() and dict[reg] != 0:
                cpt += int(lines[cpt][2])
                continue
        cpt += 1
print(dict['a'])
