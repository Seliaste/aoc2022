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

print(max(elves))