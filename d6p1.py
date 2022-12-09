

with open("input","r") as inputFile:
    lines = inputFile.readlines()
    for line in lines:
        for i in range(0,len(line)-14):
            if(len(set(line[i:i+14])) == 14):
                print(i+14)
                break;
        