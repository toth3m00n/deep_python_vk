#! /usr/bin/env python

import json
import json_utils


def main():
    json_str = '{"hello": "10", "world": "value"}'
    json_doc = json.loads(json_str)
    cjson_doc = json_utils.c_loads(json_str)
    assert json_doc == cjson_doc
    doc = json_utils.c_dumps(json_utils.c_loads(json_str))[:-1]
    assert json_str == doc


if __name__ == "__main__":
    main()
