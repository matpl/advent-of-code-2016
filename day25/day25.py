dict = {'a':0, 'b':0, 'c':0, 'd':0}

def isnumber(a):
    try:
        int(a)
    except ValueError:
        return False
    else:
        return True

with open('input.txt', 'r') as f:
    lines = [line.split(' ') for line in f]
    i = 1
    while(True):
        val = 1
        cpt = 0
        # when the prints stop, the last i is the solution
        print(i)
        dict['a'] = i
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
            elif lines[cpt][0] == 'out':
                newval = dict[lines[cpt][1].strip()]
                if newval == 1 and val == 0:
                    val = newval
                elif newval == 0 and val == 1:
                    val = newval
                else:
                    break
            cpt += 1
        i += 1
