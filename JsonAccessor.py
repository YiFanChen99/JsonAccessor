# -*- coding: utf-8 -*-
import json


def save_json(file_path, data):
    """
    Load data to json file.
    >>> save_json("./JsonAccessorDoctest.json", "{"Fuji": {"Id": 30, "server": ["JP", "CN"]}}")  # doctest: +SKIP
    """
    with open(file_path, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False)


def load_json(file_path):
    """
    Load data from json file.
    >>> result = load_json("./JsonAccessorDoctest.json")
    >>> result
    {'Fuji': {'Id': 30, 'server': ['JP', 'CN']}}
    >>> len(result['Fuji']['server'])
    2
    """
    with open(file_path, 'r', encoding='utf8') as json_data:
        return json.loads(json_data.read())


if __name__ == "__main__":
    import doctest
    doctest.testmod(report=True)
    print("Complete doctest.")
