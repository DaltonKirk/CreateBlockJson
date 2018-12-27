import os

# Declare Functions
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

def createFile(filename, delegate):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+")as newFile:
            newFile.write(delegate)
    except:
        deleteCreatedFiles()
        raise
    else:
        createdFiles.append(os.path.relpath(newFile.name))
        print("Created" + os.path.relpath(newFile.name))

def blockStatesFile():
    data = jsonStart()
    data += jsonIndent(1) + jsonKey("variants") + jsonStart()
    data += jsonIndent(2) + jsonKey("normal") + "{ " + jsonKeyValue("model", modid + ":" + blockName) + "}"
    data += jsonEnd(1)
    data += jsonEnd(0)
    return data

def modelsItemFile():
    data = jsonStart()
    data += jsonIndent(1) + jsonKeyValue("parent", modid + ":block/" + blockName) + ",\n"
    data += jsonIndent(1) + jsonKey("textures") + jsonStart()
    data += jsonIndent(2) + jsonKeyValue("layer0", modid + ":items/" + blockName)
    data += jsonEnd(1)
    data += jsonEnd(0)
    return data

def modelsBlockFile():
    data = jsonStart()
    data += jsonIndent(1) + jsonKeyValue("parent", "block/cube_all") + ",\n"
    data += jsonIndent(1) + jsonKey("textures") + jsonStart()
    data += jsonIndent(2) + jsonKeyValue("all", modid + ":blocks/" + blockName)
    data += jsonEnd(1)
    data += jsonEnd(0)
    return data

# Run Script
createdFiles = []
blockName = input("block name: ")
modid = input("modid: ")
createFile("blockstates/" + blockName + ".json", blockStatesFile())
createFile("models/item/" + blockName + ".json", modelsItemFile())
createFile("models/block/" + blockName + ".json", modelsBlockFile())
