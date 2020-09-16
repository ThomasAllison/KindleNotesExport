from pprint import pprint
from collections import defaultdict


def clippings_to_blocks(file_name):
    file = open(file_name, "r")
    all_blocks = []
    single_block = []

    for line in file:
        line = str(line).strip()
        line = line.strip('- ')

        if '======' in line:
            all_blocks.append(single_block)
            single_block = []
        elif not line:
            pass
        else:
            single_block.append(line)

    return all_blocks


def blocks_to_usable_data_structure(blocks):
    by_book = {}

    for block in blocks:
        # print(block[0])
        by_book[block[0]] = block

    return by_book


blocks = clippings_to_blocks("Example Clippings.txt")
notes_by_book = blocks_to_usable_data_structure(blocks)

pprint(blocks)
