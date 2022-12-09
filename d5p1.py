stacks = [ [] for i in range(10)]

with open("input","r") as inputFile:
    lines = inputFile.readlines()
    j = 0
    while lines[j][1] != '1':
        for i in range(9):
            if lines[j][1+i*4] != ' ':
                stacks[i].append(lines[j][1+i*4]) 
        j += 1
    for stack in stacks:
        stack.reverse()
    
    print(stacks)
    # matrix done

    j += 2
    while j < len(lines):
        line = lines[j].strip("\n").split(" ")
        for i in range(int(line[1])):
            box = stacks[int(line[3])-1].pop()
            stacks[int(line[5])-1].append(box)
        j+= 1
print(stacks)
for stack in stacks:
    if stack != []:
        print(stack[len(stack)-1],end="")
        
print()