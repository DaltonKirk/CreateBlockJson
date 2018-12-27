import os
import json

def delete_files(files):
    for filename in files:
        os.remove(filename)

def create_file(filename, data, created_files):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w+") as new_file:
            json.dump(data, new_file, indent=4)
    except:
        print("\nSomething went wrong")
        print("Deleting:", *created_files)
        print("\n")
        delete_files(created_files)
        raise
    else:
        filepath = os.path.relpath(new_file.name)
        created_files.append(filepath)
        print("Created", filepath)

def block_states(modid, block_name):
    return {
        'variants': {
            'normal': {
                'model': f'{modid}:{block_name}',
            },
        },
    }

def models_item(modid, block_name):
    return {
        'parent': f'{modid}:block/{block_name}',
        'textures': {
            'layer0': f'{modid}:items/{block_name}',
        },
    }

def models_block(modid, block_name):
    return {
        'parent': 'block/cube_all',
        'textures': {
            'all': f'{modid}:blocks/{block_name}',
        },
    }

def main(modid, block_name):    
    created_files = []
    create_file(
            f'blockstates/{block_name}.json',
            block_states(modid, block_name),
            created_files)
    create_file(
            f'models/item/{block_name}.json',
            models_item(modid, block_name),
            created_files)
    create_file(
            f'models/block/{block_name}.json',
            models_block(modid, block_name),
            created_files)

if __name__ == '__main__':
    block_name = input("block name: ")
    modid = input("modid: ")
    main(modid, block_name)