import os

createdFiles = []

def jsonStart():
    return "{\n"

def jsonEnd(indent):    
    return "\n" + jsonIndent(indent) + "}"

def jsonIndent(amount):
    amount = amount * 4
    return " " * amount

def jsonKeyValue(key, value):
    return "\"" + key + "\"" + ": " + "\"" + value + "\""

def jsonKey(key):
    return "\"" + key + "\"" + ": "

def jsonValue(value):
    return "\"" + value + "\""

def deleteCreatedFiles():
    print("\nSomething went wrong")
    for file in createdFiles:
        print("Deleting: " + file)
        os.remove(file)
    print("\n")  

blockName = input("block name: ")
modid = input("modid: ")

#Create blockstates file
try:
    filename = "blockstates/" + blockName + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+")as blockstateFile:
        blockstateFile.write(jsonStart())
        blockstateFile.write(jsonIndent(1) + jsonKey("variants") + jsonStart())
        blockstateFile.write(jsonIndent(2) + jsonKey("normal") + "{ " + jsonKeyValue("model", modid + ":" + blockName) + "}")
        blockstateFile.write(jsonEnd(1))
        blockstateFile.write(jsonEnd(0))
except:
    raise
else:
    createdFiles.append(os.path.relpath(blockstateFile.name))
    print("Created" + os.path.relpath(blockstateFile.name))


#Create models item json
try:
    filename = "models/item/" + blockName + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+") as modelsItemFile:
        modelsItemFile.write(jsonStart())
        modelsItemFile.write(jsonIndent(1) + jsonKeyValue("parent", modid + ":block/" + blockName) + ",\n")
        modelsItemFile.write(jsonIndent(1) + jsonKey("textures") + jsonStart())
        modelsItemFile.write(jsonIndent(2) + jsonKeyValue("layer0", modid + ":items/" + blockName))
        modelsItemFile.write(jsonEnd(1))
        modelsItemFile.write(jsonEnd(0))
except:
    deleteCreatedFiles()
    raise
else:
    createdFiles.append(os.path.relpath(modelsItemFile.name))
    print("Created" + os.path.relpath(modelsItemFile.name))

#Create models blocks
try:
    filename = "models/block/" + blockName + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+") as modelsBlockFile:
        modelsBlockFile.write(jsonStart())
        modelsBlockFile.write(jsonIndent(1) + jsonKeyValue("parent", "block/cube_all") + ",\n")
        modelsBlockFile.write(jsonIndent(1) + jsonKey("textures") + jsonStart())
        modelsBlockFile.write(jsonIndent(2) + jsonKeyValue("all", modid + ":blocks/" + blockName))
        modelsBlockFile.write(jsonEnd(1))
        modelsBlockFile.write(jsonEnd(0))
except:
    deleteCreatedFiles()
    raise
else:
    createdFiles.append(os.path.relpath(modelsBlockFile.name))
    print("Created" + os.path.relpath(modelsBlockFile.name))
