import json
from typing import Any

file_location = "game/configurations/ores.json"

def get_ore_configuration(ore:str) -> dict[str,float]:
    """
    Retrieves the configuration data for the provided ore type.

    ore is the name of the ore that configurations will be returned for. Must be of type string.
    """
    with open(file_location,"r") as file:
        data = file.read()
        loaded = json.loads(data)
        to_return:dict[str,Any] = loaded[ore]
    return to_return
    
"""def write_to_settings(input):
    file = open(file_location,"w")
    convert = json.dumps(input)
    file.write(convert)
    file.close()"""   
    