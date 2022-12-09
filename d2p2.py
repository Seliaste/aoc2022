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
    if chos2 == 0 :
        score += 0
        score += (chos1+2)%3+1
    elif chos2 == 1 :
        score += 3
        score += chos1+1
    elif chos2 == 2 :
        score += 6
        score +=  (chos1+1)%3+1

print(score)