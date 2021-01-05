from typing import Dict, Any
from datetime import datetime

sample = {'@pii': {'name': {'@first_name': 'Jane', '@last_name': 'Doe'},
                                   '@address': [{'@city': 'London'}, {'city': 'Moscow'}],
                                   '@id': 12345,
                                   '@email': 'jane@example.com'}}

def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    new_dict = {}

    for k, v in data.items():
        if type(k) == int:
            k = str(k)
            k = k.replace('@', '')
            k = int(k)
        else:
            if type(k) != tuple:
                k = k.replace('@', '')
        
        
        if isinstance(v, dict):
            v = rename_keys(v)
        
        elif isinstance(v, list):
            nv = rename_keys(v[0])
            nv2 = rename_keys(v[1])
            v = [nv, nv2]

        new_dict[k] = v

    return new_dict


print(rename_keys(sample))
