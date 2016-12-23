#dict = {'a':0, 'b':0, 'c':1, 'd':0}
dict = {'a':7, 'b':0, 'c':0, 'd':0}

def isnumber(a):
    try:
        int(a)
    except ValueError:
        return False
    else:
        return True

#with open('input.txt', 'r') as f:
with open('input2.txt', 'r') as f:
    lines = [line.split(' ') for line in f]
    cpt = 0
    while cpt < len(lines):
        if lines[cpt][0] == 'cpy':
            if isnumber(lines[cpt][1].strip()):
                dict[lines[cpt][2].strip()] = int(lines[cpt][1])
            else:
                dict[lines[cpt][2].strip()] = dict[lines[cpt][1].strip()]
        elif lines[cpt][0] == 'inc':
            dict[lines[cpt][1].strip()] += 1
        elif lines[cpt][0] == 'dec':
            dict[lines[cpt][1].strip()] -= 1
        elif lines[cpt][0] == 'jnz':
            reg = lines[cpt][1].strip()
            if isnumber(reg) and reg != '0' or not isnumber(reg) and dict[reg] != 0:
                if not isnumber(lines[cpt][2].strip()):
                    cpt += int(dict[lines[cpt][2].strip()])
                else:
                    cpt += int(lines[cpt][2])
                continue
        elif lines[cpt][0] == 'tgl':
            ins = dict[lines[cpt][1].strip()]
            if cpt + ins < len(lines) and cpt + ins > 0:
                if len(lines[cpt + ins]) == 2:
                    if lines[cpt + ins][0] == 'inc':
                        lines[cpt + ins][0] = 'dec'
                    else:
                        lines[cpt + ins][0] = 'inc'
                else:
                    if lines[cpt + ins][0] == 'jnz':
                        lines[cpt + ins][0] = 'cpy'
                    else:
                        lines[cpt + ins][0] = 'jnz'
        cpt += 1
print(dict['a'])
