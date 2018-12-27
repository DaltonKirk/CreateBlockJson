import os, json

# Declare Functions
def deleteCreatedFiles():
    print("\nSomething went wrong")
    for file in createdFiles:
        print("Deleting: " + file)
        os.remove(file)
    print("\n")

def createFile(filename, data):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as newFile:
            jstr = json.dumps(data, indent=4)
            newFile.write(jstr)
    except:
        deleteCreatedFiles()
        raise
    else:
        createdFiles.append(os.path.relpath(newFile.name))
        print("Created" + os.path.relpath(newFile.name))

def blockStatesFile():
    return {
        'variants': {
            'normal': {
                'model': f"{modid}:{blockName}"
            }
        }
    }

def modelsItemFile():
    return {
        'parent': f"{modid}:block/{blockName}",
        'textures': {
            'layer0': f"{modid}:items/{blockName}"
        }
    }

def modelsBlockFile():
    return {
        'parent': 'block/cube_all',
        'textures': {
            'all': f"{modid}:blocks/{blockName}"
        }
    }

# Run Script
createdFiles = []
blockName = input("block name: ")
modid = input("modid: ")
createFile(f"blockstates/{blockName}.json", blockStatesFile())
createFile(f"models/item/{blockName}.json", modelsItemFile())
createFile(f"models/block/{blockName}.json", modelsBlockFile())