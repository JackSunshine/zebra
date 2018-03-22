# -*- coding: utf-8 -*

file = "stocks.tmp"


def write_string_to_file(messages):
    with open(file, 'w') as f:
        f.write("%s", messages)
