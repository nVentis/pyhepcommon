from json import load
from typing import Optional

def json_file_readable(file_path:str) -> bool:
    result = False
    try:
        with open(file_path) as jf:
            j = load(jf)
            
        result = True
        
    except Exception as e:
        result = False
        
    return result