import json

file_location = "Configurations\\Ores.json"

def get_ore_configuration(ore):
    """
    Retrieves the configuration data for the provided ore type.

    ore is the name of the ore that configurations will be returned for. Must be of type string.
    """
    file = open(file_location,"r")
    data = file.read()
    loaded = json.loads(data)
    to_return = loaded[ore]
    file.close()
    return to_return
    
"""def write_to_settings(input):
    file = open(file_location,"w")
    convert = json.dumps(input)
    file.write(convert)
    file.close()"""   
    