from collections import defaultdict
from pprint import pprint


def clippings_to_blocks(file_name):
    file = open(file_name, "r", encoding="utf-8-sig")
    lines = [line.rstrip() for line in file]
    file.close()

    blocks = []
    block = []
    for line in lines:
        if line == '==========':
            blocks.append(block)
            block = []
        elif line == '':
            pass
        else:
            block.append(line)

    return blocks


def blocks_to_usable_data_structure(blocks):
    by_book = defaultdict(list)

    for block, next_block in zip(blocks, blocks[1:] + [blocks[0]]):
        title = block[0]
        kind = block[1]
        content = block[2]

        next_kind = next_block[1]
        next_content = next_block[2]

        if '- Your Highlight' in kind:
            location = kind[kind.find("Highlight on ")+len("Highlight on "):kind.rfind(" | ")]
            note = dict(highlight=content, location=location.split(' | ')[0])

            if '- Your Note' in next_kind:
                note['note'] = next_content

            by_book[title].append(note)

    return by_book


def write_to_files(usable_data):
    for book, highlights in usable_data.items():
        file = open('./output/{}.md'.format(book), 'w')
        file.write("- Highlights & Notes\n")

        for h in highlights:
            if 'page' in h['location']:
                file.write("    - ({}) {}\n".format(h['location'], h['highlight']))
            else:
                file.write("    - {}\n".format(h['highlight']))

            if h.get('note'):
                file.write("        - {}\n".format(h['note']))

        file.close()


blocks_output = clippings_to_blocks("Example Clippings.txt")
usable_data = blocks_to_usable_data_structure(blocks_output)
write_to_files(usable_data)

