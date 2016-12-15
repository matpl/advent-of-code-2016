import hashlib

input = 'ihaygndm'
cpt = 0
keys = []
dict = {}

#iter = 1
iter = 2017

def gethash(h):
    for i in range(iter):
        m2 = hashlib.md5()
        m2.update(h.encode('utf8'))
        h = m2.hexdigest()
    return h

def isvalid(i, car):
    for k in range(i + 1, i + 1001):
        if k in dict:
            digest2 = dict[k]
        else:
            digest2 = gethash(str(input) + str(k))
            dict[k] = digest2
        for n in range(len(digest2)-4):
            if digest[j] == digest2[n] == digest2[n+1] == digest2[n+2] == digest2[n+3] == digest2[n+4]:
                return True
    return False

while(len(keys) != 64):
    m = hashlib.md5()
    if cpt in dict:
        digest = dict[cpt]
    else:
        digest = gethash(str(input) + str(cpt))
        dict[cpt] = digest
    for j in range(len(digest)-2):
        if digest[j] == digest[j+1] == digest[j+2]:
            if isvalid(cpt, digest[j]):
                keys.append(cpt)
            break
    cpt += 1

print(keys[-1])
