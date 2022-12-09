with open("input","r") as inputFile:
    priosum = 0
    parsed = [x.strip("\n") for x in inputFile.readlines()]
    for i in range(0,len(parsed)//3):
        alrdyseen = []
        for char in parsed[i*3]:
            if char not in alrdyseen and char in parsed[i*3+1] and char in parsed[i*3+2]:
                if char.islower():
                    priosum += ord(char)-96
                if char.isupper():
                    priosum += ord(char)-64+26
            alrdyseen.append(char)
print(priosum)