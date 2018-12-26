import os

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

print("input block name")
blockName = input()

print("input modid")
modid = input()

#Create Blockstates
filename = "blockstates/" + blockName + ".json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f2 = open(filename, "w+")
f2.write(jsonStart())
f2.write(jsonIndent(1) + jsonKey("variants") + jsonStart())
f2.write(jsonIndent(2) + jsonKey("normal") + "{ " + jsonKeyValue("model", modid + ":" + blockName) + "}")
f2.write(jsonEnd(1))
f2.write(jsonEnd(0))

#Create models item json
filename = "models/item/" + blockName + ".json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, "w+")
f.write(jsonStart())
f.write(jsonIndent(1) + jsonKeyValue("parent", modid + ":block/" + blockName) + ",\n")
f.write(jsonIndent(1) + jsonKey("textures") + jsonStart())
f.write(jsonIndent(2) + jsonKeyValue("layer0", modid + ":items/" + blockName))
f.write(jsonEnd(1))
f.write(jsonEnd(0))

#Create models blocks
filename = "models/block/" + blockName + ".json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f3 = open(filename, "w+")
f3.write(jsonStart())
f3.write(jsonIndent(1) + jsonKeyValue("parent", "block/cube_all") + ",\n")
f3.write(jsonIndent(1) + jsonKey("textures") + jsonStart())
f3.write(jsonIndent(2) + jsonKeyValue("all", modid + ":blocks/" + blockName))
f3.write(jsonEnd(1))
f3.write(jsonEnd(0))