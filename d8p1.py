matrix= [(list(map(int,list(line.strip("\n"))))) for line in open("input",'r').readlines()]

res = 0 
for y in range(1,len(matrix)-1):
    for x in range(1,len(matrix[y])-1):
        left = matrix[y][:x]
        left.reverse()
        right = matrix[y][x+1:]
        top = []
        down = []
        for row in matrix[:y]:
            top.append(row[x])
        top.reverse()
        for row in matrix[y+1:]:
            down.append(row[x])
        score = 1
        for direction in [left,right,top,down]:
            i = 0
            while(i+1 < len(direction) and direction[i] < matrix[y][x]):
                i += 1
            score *= i+1
            
        if (score > res):
            res = score

print(res)