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
        nb = int(line[1])
        stack1 = int(line[3])-1
        stack2 = int(line[5])-1
        boxes = stacks[stack1][len(stacks[stack1])-nb:]
        for i in range(nb):
            stacks[stack1].pop()
        for box in boxes:
            stacks[stack2].append(box)
        j+= 1
print(stacks)
for stack in stacks:
    if stack != []:
        print(stack[len(stack)-1],end="")
        
print()