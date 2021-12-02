count = 0
masterlist = []

with open('input.txt') as f:
    while f:
        sonartxt = f.readline()
        if sonartxt != "":
            sonardat = int(sonartxt.rstrip("\n"))    
            masterlist.append(sonardat)
        else:
            break

listoflists = []
i = 0

while True:
    try:
        listoflists.append([masterlist[i], masterlist[i+1], masterlist[i+2]])
        i += 1
    except:
        break
i = 0

while True:
    try:
        if sum(listoflists[i]) < sum(listoflists[i+1]):
            count += 1
            i += 1
        else:
            i += 1
    except:
        break

print(count)
