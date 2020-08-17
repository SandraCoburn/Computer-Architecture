"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 
        self.pc = 0 
        self.reg = [0] * 8
        self.running = False
        

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
          # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def ram_read(self, counter):
        return self.ram[counter]
    def ram_write(self, counter, MDR): #MDR value
        self.reg[counter] = MDR
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        #  0b10000010 
        self.running = True
        pc = self.pc
        print("running")
        print("Register", self.reg)
        #Add the HLT instruction definition
        HLT = 0b00000001 
        LDI = 0b10000010
        PRN = 0b01000111

        while self.running:
            
            #Instruction Register. Read memory address stored in pc
            ir = self.ram_read(pc)
            print("ir", ir)
            if ir == HLT:
                #exit the program
                self.running = False
                pc += 1
                #sys.exit()
            if ir == LDI:
                #This instruction sets a specified register to a specified value,
                # set the value to an integer
                print(self.ram_read(pc+1))
                self.ram_write(self.ram_read(pc+1), self.ram_read(pc+2))
                print("LDI, pc, pc+1", ir, self.ram_read(pc+1), self.ram_read(pc+2))
                
                pc += 3
            if ir == PRN:
                #Print to the console the decimal integer value that is stored in the given register
                print(self.ram_read(pc+1))
                print("Register, ram: ", self.reg, self.ram)
                pc += 2


