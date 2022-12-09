with open("input","r") as inputFile:
    res = 0
    for line in [x.strip("\n") for x in inputFile.readlines()]:
        pairs = line.split(",")
        pairs = [list(map(int,pair.split("-"))) for pair in pairs]
        if (pairs[0][0] >= pairs[1][0] and pairs[0][0] <= pairs[1][1]) or (pairs[0][1] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]) or (pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]) or (pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1]):
            res+=1
            print(pairs)
print(res)