import hashlib

input = 'ugkcyxxp'
i = 0
password = [None] * 8

while(None in password):
    m = hashlib.md5()
    m.update((str(input) + str(i)).encode('utf-8'))
    digest = m.hexdigest()
    if(digest[:5] == '00000'):
        pos = ord(digest[5]) - 48
        if 0 <= pos <= 7 and password[pos] is None:
            password[pos] = digest[6]
    i += 1

print(''.join(password))
