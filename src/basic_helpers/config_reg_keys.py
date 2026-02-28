from itertools import product
from typing import TypedDict
from typing_extensions import NotRequired

class RegParams(TypedDict):
    rows: str
    cols: str
    testrows: str
    testcols: str
    extra: NotRequired[list[tuple[str, str]]]


REG_KEYS: dict[str, RegParams] = {'DACH': {'rows': '9ABCDEFGHIJK', 'cols': 'DEFGHIJKLMNOPQRST', 'testrows': '9A', 'testcols': 'LM'}, 
            'SUD': {'rows': '012345678yz', 'cols': 'GHIJKLMNOPQRST', 'testrows': '78', 'testcols': 'MN'}, 
            'IBERIA': {'rows': '012345678', 'cols': '0123456789ABCDEF', 'testrows': '01', 'testcols': '789'}, 
            'WNW': {'rows': '9ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'cols': '0123456789ABC', 'testrows': 'AB', 'testcols': 'AB'}, 
            'SCAN': {'rows': 'LMNOPQRSTUVWXYZ', 'cols': 'DEFGHIJKLMNOPQRSTUVWXYZabcdefg', 'testrows': 'NO', 'testcols': 'NO'}, 
            'OST': {'rows': '6789ABCDEFGHIJK', 'cols': 'UVWXYZabcdef', 'testrows': 'DE', 'testcols': 'VW'}, 
            'SUDEST': {'rows': '012345yz', 'cols': 'UVWXYZabcdefghijklmnopqrst', 'testrows': '34', 'testcols': 'ij', 
                       'extra': [('6', 'i'), ('6', 'j'), ('6', 'k')]}, 
           }

REV_REG_KEYS: dict[str, str] = {}

for reg_key, vals in REG_KEYS.items():
    for r, c in product(vals['rows'], vals['cols']):
        REV_REG_KEYS[f"{r}{c}"] = reg_key
    if 'extra' in vals:
        for r, c in vals['extra']:
            REV_REG_KEYS[f"{r}{c}"] = reg_key

