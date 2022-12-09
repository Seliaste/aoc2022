file = open("input","r")
lines = file.readlines()

elves = [0]*1000
i = 0
for line in lines:
    line = line.strip("\n")
    if line == "":
        i+=1
    else:
        elves[i] += int(line)

max1 = max(elves)
elves.remove(max1)
max2 = max(elves)
elves.remove(max2)
max3 = max(elves)
print(max1+max2+max3)