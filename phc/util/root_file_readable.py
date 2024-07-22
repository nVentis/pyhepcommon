import uproot as ur
from typing import Optional

def root_file_readable(file_path:str, tree_name:Optional[str]=None) -> bool:
    result = False
    try:
        with ur.open(file_path) as file:
            if isinstance(tree_name, str):
                tree = file[tree_name]
                rf_keys = tree.keys()

                result = len(tree[rf_keys[0]].array()) > 0
            else:
                result = True
            
    except Exception as e:
        result = False
        
    return result