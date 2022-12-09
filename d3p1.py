with open("input","r") as inputFile:
    priosum = 0
    for line in [x.strip("\n") for x in inputFile.readlines()]:
        alrdyseen = []
        firstHalf = line[0:len(line)//2]
        secondHalf = line[len(line)//2:]
        for char in firstHalf:
            if char not in alrdyseen and char in secondHalf:
                if char.islower():
                    priosum += ord(char)-96
                if char.isupper():
                    priosum += ord(char)-64+26
            alrdyseen.append(char)
    print(priosum)