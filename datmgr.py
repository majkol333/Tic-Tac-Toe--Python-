import os

gameData = {
    "uwins":0,
    "cwins":0,
    "draws":0,
}
victory = "You won!"; loss = "You lost!"; draw = "It's a draw!"

def save(filePath: str, content: str):
    with open(filePath, 'w') as file:
        file.write(content)
def loadint(filePath: str):
    ret = None
    with open(filePath) as file:
        ret = file.read()
    if ret.isdigit():
        return int(ret)
    else:
        return None
def addTo(keyword: str):
    if not keyword:
        return
    
    global gameData
    try:
        gameData[keyword]+=1
    except KeyError:
        print(f"Game error, saveVar name '{keyword}' not found in data")
        return
    
    if keyword == "uwins":
        print(victory)
    elif keyword == "cwins":
        print(loss)
    elif keyword == "draws":
        print(draw)
    else:
        print("Unknown game turnout")
    save(os.path.join(dataFolder, keyword+".dat"),str(gameData[keyword]))


dataFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gameData")
if not (os.path.exists(dataFolder) and os.path.isdir(dataFolder)):
    os.mkdir(dataFolder)
files = {}
for entry in gameData:
    entryFile = os.path.join(dataFolder, entry+".dat")
    files[entry] = entryFile
    if not (os.path.exists(entryFile) and os.path.isfile(entryFile)):
        save(entryFile, str(gameData[entry]))
    else:
        gameData[entry] = loadint(os.path.join(dataFolder, entry+".dat"))