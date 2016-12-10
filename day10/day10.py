class Output:
    def __init__(self, no):
        self.no = no
        self.values = []

    def add(self, no):
        self.values.append(no)
    
class Bot(Output):
    def __init__(self, no):
        super().__init__(no)
        self.lowaction = None
        self.highaction = None
        
    def add(self, no):
        super(Bot, self).add(int(no))
        if len(self.values) == 2:
            self.distribute()

    def distribute(self):
        self.values = sorted(self.values)
        
        if self.values[0] == 17 and self.values[1] == 61:
            print(self.no)
        
        if self.lowaction is not None and self.highaction is not None:
            self.lowaction.add(self.values[0])
            self.highaction.add(self.values[1])
            self.values = []

dict = {}

def getobj(name, no):
    if (name + no) not in dict:
        dict[name + no] = globals()[name[0].capitalize() + name[1:]](no)
    return dict[name + no]

with open('input.txt', 'r') as f:
    for line in f:
        words = line.split(' ')
        if(words[0] == 'value'):
            bot = getobj(words[4], str(int(words[5])))
            bot.add(words[1])
        else:
            bot = getobj(words[0], words[1])
            bot.lowaction = getobj(words[5], str(int(words[6])))
            bot.highaction = getobj(words[10], str(int(words[11])))

for w in dict:
    if 'bot' in w and len(dict[w].values) == 2:
        dict[w].distribute()

print(dict['output0'].values[0] * dict['output1'].values[0] * dict['output2'].values[0])
