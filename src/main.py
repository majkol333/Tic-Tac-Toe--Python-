import datmgr
import field
from os import system

def readclear(inp: str = "Press Enter to continue\n"):
    input(inp); system("cls")
system("cls")
if __name__ == "__main__":
    game = field.Field(3, 3)
    turnout = None
    
    print("───────── TIC TAC TOE ─────────")
    readclear()
    print("""───── SIGNS ──────
X => Player's moves
O => Computer's moves
- => Empty places""")
    readclear()
    print("───── MOVE ─────")
    game.display()
    print("""To make a move, write the coordinates of the place you want to take.
Example: A1""")
    readclear("Press Enter to start playing\n")

    while not turnout:
        system("cls")
        game.display()
        turnout = game.turnout()
        if turnout:
            datmgr.addTo(turnout.value)
            print(f"""
STATS
Wins: {datmgr.loadint(datmgr.files["uwins"])}
Loses: {datmgr.loadint(datmgr.files["cwins"])}
Draws: {datmgr.loadint(datmgr.files["draws"])}
""")
            if input("Play again? (ignore if yes, 'n' if no): ").lower().strip() == "n":
                break
            else:
                system("cls")
                turnout = None
                game.__init__(3,3)
                continue
        inp = None
        while not inp:
            inp = input("Your move: ").strip().upper()
            if not game.replace(inp):
                inp = None
        game.computer()