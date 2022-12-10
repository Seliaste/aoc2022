visited = []
nodes = [[0,0] for i in range(10)]

def compute_tail_pos():
    global nodes
    for i in range(1,10):
        if abs(nodes[i-1][0]-nodes[i][0]) > 1 :
            nodes[i][0] += (nodes[i-1][0]-nodes[i][0])//2
            if abs(nodes[i-1][1]-nodes[i][1]) > 0 : 
                nodes[i][1] += (nodes[i-1][1]-nodes[i][1])//abs(nodes[i-1][1]-nodes[i][1])
        elif abs(nodes[i-1][1]-nodes[i][1]) > 1 :
            nodes[i][1] += (nodes[i-1][1]-nodes[i][1])//2
            if abs(nodes[i-1][0]-nodes[i][0]) > 0 : 
                nodes[i][0] += (nodes[i-1][0]-nodes[i][0])//abs(nodes[i-1][0]-nodes[i][0])
            
    


instructions = [line.strip("\n").split(" ") for line in open("input",'r').readlines()]

for instruction in instructions:
    for i in range(int(instruction[1])):
        match instruction[0]:
            case "U":
                nodes[0][1]+=1

            case "L":
                nodes[0][0]-=1
            
            case "R":
                nodes[0][0]+=1

            case "D":
                nodes[0][1]-=1
        compute_tail_pos()
        if tuple(nodes[9]) not in visited:
            visited.append(tuple(nodes[9]))
    
print(len(visited))