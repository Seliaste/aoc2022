file = open("input","r")
lines = file.readlines()

score = 0

for line in lines:
    line = line.strip("\n").split(" ")

    if line[0] == 'A':
        chos1 = 0
    elif line[0] == 'B':
        chos1 = 1
    elif line[0] == 'C':
        chos1 = 2
    if line[1] == 'X':
        chos2 = 0
    elif line[1] == 'Y':
        chos2 = 1
    elif line[1] == 'Z':
        chos2 = 2
    if chos1 == chos2 :
        score += 3
    elif chos1 - chos2 == -1 or chos1 - chos2 == 2 :
        score += 6
    elif chos1 - chos2 == 1 or chos1 - chos2 == -2 :
        score += 0
    score += chos2+1

print(score)