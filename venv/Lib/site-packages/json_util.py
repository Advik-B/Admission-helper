import json as __json
import os as __os

global validate_json, minify_json, largeify_json, preetify_json, write_json, convert_json


class json_modes():
    def __init__(self):
        self.JSON_TO_DICT = 1
        self.DICT_TO_JSON = 2

class Json_Object(type): pass
class OverWriteModeError(Exception): pass
class ModeError(Exception): pass

def validate_json(json_data) -> True|False:
    try:
        __json.loads(data)
    except ValueError:
        return False
    return True

def minify_json(json_data):
    "Minify JSON"
    json_data = __json.loads(json_data) # store in __json structure
    json_string = __json.dumps(json_data, separators=(',', ":")) # Compact JSON structure
    return json_string

def largeify_json(json_data, indent_size: int) -> Json_Object:
    json_obj = __json.loads(json_data)
    return __json.dumps(json_obj, indent=indent_size)

def preetify_json(json_data, indent_size: int=4) -> Json_Object:
    json_obj = __json.loads(json_data)
    return __json.dumps(json_obj, indent=indent_size)

def write_json(
    Json_Data: Json_Object,
    file_name: str,
    overwrite: bool,
    indent_size: int=0,
    ):
    """\n
    Will write to json file with the args provided
    
    Args:
        Json_Data (`Json_Object`): The Data for updating the json file
        file_name (`str`): The json file path/file name. A new one will be created if it does not exist
        overwrite (`bool`): Weather to overwrite the json Data or append it
    """
    if __os.path.isfile(file_name):
        if overwrite == True:
            if not indent_size or indent_size <= 0:
                with open(file_name , 'w+') as dat:
                    dat.write(Json_Data)
            
            else:
                json_dict = __json.loads(Json_Data)
                json_data = __json.dumps(json_dict, indent=indent_size)
                with open(file_name , 'w+') as dat:
                    dat.write(json_data)
        
        elif not overwrite:
            if not indent_size or indent_size <= 0:
                with open(file_name, 'r') as O:
                    existing_json_dict = __json.load(O)
                new_json_dict = __json.loads(Json_Data)
                
                for key, val in new_json_dict.items():
                    existing_json_dict.update({key:val})
                
                final_json_data = __json.dumps(existing_json_dict)
                with open(file_name, 'w+') as file:
                    file.write(final_json_data)
            
            else:
                with open(file_name, 'r') as O:
                    existing_json_dict = __json.load(O)
                new_json_dict = __json.loads(Json_Data)
                
                for key, val in new_json_dict.items():
                    existing_json_dict.update({key:val})
                
                final_json_data = __json.dumps(existing_json_dict, indent=indent_size)
                with open(file_name, 'w+') as file:
                    file.write(final_json_data)
        else:
            raise OverWriteModeError(f'The overwrite mode {overwrite} is not valid\nIt only accepts True/False').with_traceback(None)
    else:
        if overwrite == True or overwrite == False:
            if not indent_size or indent_size <= 0:
                with open(file_name , 'w+') as dat:
                    dat.write(Json_Data)
            
            else:
                json_dict = __json.loads(Json_Data)
                json_data = __json.dumps(json_dict, indent=indent_size)
                with open(file_name , 'w+') as dat:
                    dat.write(json_data)
        else: raise OverWriteModeError(f'The overwrite mode {overwrite} is not valid\nIt only accepts True/False').with_traceback(None)

def convert_json(data: any, mode: int) -> any:
    """Coverts json data into dict object or vice versa

    Args:
        data: The raw json data/dict
        
        mode:
            The modes:
                1: json to dict
                2: dict to json

    Returns:
        dict/json: the converted result
    """
    global DICT_TO_JSON
    global JSON_TO_DICT
    JSON_TO_DICT = 1
    DICT_TO_JSON = 2
    if mode == JSON_TO_DICT:
        return __json.loads(data)
    elif mode == DICT_TO_JSON:
        return __json.dumps(data)
    else: raise ModeError(f'{mode} is not a valid mode').with_traceback(None)
