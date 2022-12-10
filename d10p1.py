class CPU:
    cycle = 0
    X = 1
    sig_strengths = []
    def addx(self,val):
        self.cycle += 1
        self.compute_sigstrength()
        self.cycle += 1
        self.compute_sigstrength()
        self.X += val
    
    def noop(self):
        self.cycle += 1
        self.compute_sigstrength()
    
    def compute_sigstrength(self):
        if (self.cycle+20)%40 == 0:
            self.sig_strengths.append(self.X * self.cycle)       

instructions = [line.strip("\n").split(" ") for line in open("input",'r').readlines()]

cpu = CPU()

for instruction in instructions:
    match instruction[0]:
        case "addx":
            cpu.addx(int(instruction[1]))
        case "noop":
            cpu.noop()

print(cpu.cycle)
print(cpu.X)
print(cpu.sig_strengths)
print(sum(cpu.sig_strengths[0:6]))