length = 35651584
input = '10001110011110000'

def getchecksum(s):
    cs = ''
    for i in range(int(len(s) / 2)):
        if s[i*2]  == s[i*2 + 1]:
            cs += '1'
        else:
            cs += '0'
    return cs

def getresult(a):
    b = a
    b1 = b[::-1]
    c = ''
    for car in b1:
        if car == '0':
            c = c + '1'
        else:
            c = c + '0'
    return a + '0' + c

while len(input) < length:
    input = getresult(input)[:length]

ck = getchecksum(input)
while len(ck) % 2 == 0:
    ck = getchecksum(ck)
    
print(ck)
