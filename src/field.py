from enum import Enum
from random import randint
from string import ascii_uppercase as ascii

class Turnout(Enum):
    UWIN = "uwins"
    CWIN = "cwins"
    DRAW = "draws"

class Field:
    # Constructor
    def __init__(self, width:int, height:int):
        self.area = []
        for i in range(height):
            self.area.append(list())
            for j in range(width):
                self.area[i].append('-')

    # Display all place in field object
    def display(self):
        print(end="    ") # ASCII
        for i in range(len(self.area[0])):
            if len(ascii) > i:
                print(ascii[i], end=" ")
        print(end="\n  ")
        rng=2*len(self.area[0])+3 # TOP
        for i in range(rng):
            if i==0:
                print(end='┌')
            elif i==rng-1:
                print(end='┐')
            else:
                print(end='─')
        print()
        k=1 # NUM + VALUES
        for i in self.area: 
            print(k, end=' ')
            print(end='│ ')
            for j in i:
                print(j, end=" ")
            print('│')
            k+=1
        print(end="  ")
        rng=2*len(self.area[0])+3 # BOTTOM
        for i in range(rng):
            if i==0:
                print(end='└')
            elif i==rng-1:
                print(end='┘')
            else:
                print(end='─')
        print()
    

    # Occupy a place (for user moves)
    def replace(self, inp:str):
        if not (
            len(inp) >= 2 and  # Correct inp length
            inp[0] in ascii and # First symbol is an ascii letter (j index)
            (inp[1:]).isdigit() and # Rest is digits (i index)
            ascii.index(inp[0]) <= len(self.area) and # j index in bound
            int(inp[1:]) <= len(self.area[0]) # i index in bound
        ):
            print("Invalid input.")
            return False
        i, j = int(inp[1:])-1, ascii.index(inp[0])
        if self.area[i][j] == "-":
            self.area[i][j] = "X"
            return True
        else:
            print("Place already taken")
            return False
    
    # Occupy random place (for computer moves)
    def computer(self):
        if self.turnout():
            return
        while True:
            i, j = randint(0, len(self.area)-1), randint(0, len(self.area[0])-1)
            if self.area[i][j] == '-':
                self.area[i][j] = 'O'
                break
    
    # Find count of given symbols in field
    def find(self, symb:str):
        ret = 0
        for i in self.area:
            if i.count(symb):
                ret+=i.count(symb)
        return ret
    
    def symVictory(self, sym:str) -> bool:
        directions = [
            (1, 0), # down
            (0, 1), # right
            (1, 1), # down-right
            (1, -1) # down-left
        ]
        for i in range(len(self.area)):
            for j in range(len(self.area)):
                if self.area[i][j] == sym:
                    for i_step, j_step in directions:
                        i_next, j_next = i + i_step, j + j_step
                        i_next2, j_next2 = i + 2*i_step, j + 2*j_step

                        if (
                            0 <= i_next < 3 and 0 <= j_next < 3 and
                            0 <= i_next2 < 3 and 0 <= j_next2 < 3 and
                            self.area[i_next][j_next] == sym and
                            self.area[i_next2][j_next2] == sym 
                        ):
                            return True
        return False
    
    def turnout(self) -> Turnout:
        if self.symVictory('X'):
            return Turnout.UWIN
        elif self.symVictory('O'):
            return Turnout.CWIN
        elif self.find('-') < 2:
            return Turnout.DRAW