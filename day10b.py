# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

class Machine:
    def __init__(self, instructions: list[str]):
        self.x = 1
        self.pc = 0
        self.blocked = False
        self.instructions = instructions
    
    def exec_instruction(self):
        ins = self.instructions[self.pc]
        if ins == "noop":
            self.pc += 1
            return
        ins = ins.split()
        if ins[0] == "addx":
            if not self.blocked:
                self.blocked = True
                return
            self.blocked = False
            self.x += int(ins[1])
            self.pc += 1


with open('day10.dat') as f:
    instructions = [x.strip() for x in f.readlines() if x.strip() != ""]


machine = Machine(instructions)
output = ''
for i in range(240):
    pixel = i % 40
    if machine.x - 1 <= pixel <= machine.x + 1:
        output += '#'
    else:
        output += '.'
    if pixel % 40 == 39:
        output += '\n'
    machine.exec_instruction()

print(output)
