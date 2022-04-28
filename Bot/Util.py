import json
#-----------------------------------------------------------------------
def load_Json(path:str) -> json:
    # Load Json file
    with open(path, 'r') as j:
        _json = json.load(j)
    print(f'Json File: {path} (loaded)') 
    return _json
#-----------------------------------------------------------------------