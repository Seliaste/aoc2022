class CPU:
    cycle = 0
    X = 1
    def addx(self,val,crt):
        crt.draw_pixel(self)
        self.cycle += 1
        crt.draw_pixel(self)
        self.cycle += 1
        self.X += val
    
    def noop(self,crt):
        crt.draw_pixel(self)
        self.cycle += 1
        

class CRT:
    screen = [["."]*40 for i in range(7)]

    def print_screen(self):
        for row in self.screen:
            print(row)
    def draw_pixel(self,cpu):
        print(cpu.cycle//40,cpu.cycle%40)
        self.screen[cpu.cycle//40][cpu.cycle%40] = "#" if abs(cpu.cycle%40-cpu.X) <= 1 else "."

            

instructions = [line.strip("\n").split(" ") for line in open("input",'r').readlines()]

cpu = CPU()
crt = CRT()

for instruction in instructions:
    match instruction[0]:
        case "addx":
            cpu.addx(int(instruction[1]),crt)
        case "noop":
            cpu.noop(crt)

print(crt.print_screen())