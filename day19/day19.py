no = 3014603
arr = [i for i in range(no)]
i = 0

#while len(arr) != 1:
#    if len(arr) % 2 != 0:
#        arr = arr[::2][-1:] + arr[::2][:-1]
#    else:
#        arr = arr[::2]

while len(arr) != 1:
    if i >= len(arr):
        i = 0

    toremove = int(len(arr) / 2 + i) % len(arr)
    arr.pop(toremove)
    if toremove > i:
        i += 1
    
print(arr[0] + 1)
