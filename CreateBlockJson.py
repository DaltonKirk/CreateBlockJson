import os

# Declare Functions
def jsonStart():
    return "{\n"

def jsonEnd(indent = 0):    
    return "\n" + jsonIndent(indent) + "}"

def jsonIndent(amount):
    amount = amount * 4
    return " " * amount

def jsonKeyValue(key, value, indent = 0):
    return jsonIndent(indent) + jsonKey(key) + jsonValue(value)

def jsonKey(key, indent = 0):
    return jsonIndent(indent) + "\"" + key + "\"" + ": "

def jsonValue(value):
    return "\"" + value + "\""

def deleteCreatedFiles():
    print("\nSomething went wrong")
    for file in createdFiles:
        print("Deleting: " + file)
        os.remove(file)
    print("\n")

def createFile(filename, data):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+")as newFile:
            newFile.write(data)
    except:
        deleteCreatedFiles()
        raise
    else:
        createdFiles.append(os.path.relpath(newFile.name))
        print("Created" + os.path.relpath(newFile.name))

def blockStatesFile():
    data = jsonStart()
    data += jsonKey("variants", 1) + jsonStart()
    data += jsonKey("normal", 2) + "{ " + jsonKeyValue("model", modid + ":" + blockName) + "}"
    data += jsonEnd(1)
    data += jsonEnd()
    return data

def modelsItemFile():
    data = jsonStart()
    data += jsonKeyValue("parent", modid + ":block/" + blockName, 1) + ",\n"
    data += jsonKey("textures", 1) + jsonStart()
    data += jsonKeyValue("layer0", modid + ":items/" + blockName, 2)
    data += jsonEnd(1)
    data += jsonEnd()
    return data

def modelsBlockFile():
    data = jsonStart()
    data += jsonKeyValue("parent", "block/cube_all", 1) + ",\n"
    data += jsonKey("textures", 1) + jsonStart()
    data += jsonKeyValue("all", modid + ":blocks/" + blockName, 2)
    data += jsonEnd(1)
    data += jsonEnd()
    return data

# Run Script
createdFiles = []
blockName = input("block name: ")
modid = input("modid: ")
createFile("blockstates/" + blockName + ".json", blockStatesFile())
createFile("models/item/" + blockName + ".json", modelsItemFile())
createFile("models/block/" + blockName + ".json", modelsBlockFile())
