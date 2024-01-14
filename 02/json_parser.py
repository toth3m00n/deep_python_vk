"""Json-parser"""

import json


def name_handler(name: str, field: str):
    """function-handler"""

    print(f"Yo! The '{name}' was found in {field}!")


def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    """Parsing json and execute function for founded word"""

    json_doc = json.loads(json_str)
    for field in required_fields:
        try:
            current_key = json_doc[field]
            list_of_words = current_key.split()
            for word in keywords:
                if word in list_of_words:
                    keyword_callback(word, field)
        except KeyError:
            print(f"{field} not in json string")


if __name__ == "__main__":
    JSON_STR = '{"key1": "Word1 word2", "key2": "word2 word3", "key3": "word3"}'
    parse_json(JSON_STR, name_handler, ["key1", "key3"], ["word2", "word3"])
