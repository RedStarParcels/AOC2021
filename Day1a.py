count = 0
previousdat = 0

with open('input.txt') as f:
    while f:
        sonartxt = f.readline()
        if sonartxt != "":
            sonardat = int(sonartxt.rstrip("\n"))
            if previousdat != 0:
                if sonardat > previousdat:
                    previousdat = sonardat
                    count+=1
                else:
                    previousdat = sonardat
            else:
                previousdat = sonardat
        else:
            break

print(count)
