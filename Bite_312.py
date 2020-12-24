import builtins
import keyword
import sys
from importlib import import_module
from typing import Dict, List

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    total = 0
    built_ins = dir(builtins)
    keywords = [k for k in keyword.kwlist]
    modules = [k for k in sys.modules.keys()]
    modules.extend(['pytest'])

    for name in objects:
        if name in built_ins:
            total += scores.get('builtin')
        if name in keywords:
            total += scores.get('keyword')
        try:
            if name in modules or import_module(name):
                total += scores.get('module')
        except:
            pass
        
    return total


x = ['hashlib', 'base64', 'nonlocal']
print(score_objects(x))

