import copy

# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0],
# ]
# matrix = [
#     [1, 0, 1, 1, 0],
#     [1, 0, 0, 1, 1],
# ]
matrix = [
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]


class River(object):
    identifier = 1
    blocks = []

    def __init__(self):
        self.blocks = []

    @classmethod
    def is_river_block(self, item):
        return item == self.identifier

    def is_block_in_river(self, block):
        return block in self.blocks

    def append(self, block):
        self.blocks.append(block)

    def merge(self, river):
        self.blocks.extend(river.blocks)

    def __repr__(self):
        return (
            "River("
            + ", ".join([block.__repr__() for block in self.blocks])
            + ")"
        )


class RiverBlock(object):
    row = -1
    col = -1

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return "Block({}, {})".format(self.row, self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


def block_in_rivers(rivers, river_block):
    for river in rivers:
        if river.is_block_in_river(river_block):
            return True

    return False


def get_river_of_block(rivers, river_block):
    for river in rivers:
        if river.is_block_in_river(river_block):
            return river

    return None


def is_river_in_rivers(river_to_find):
    for river in rivers:
        if river_to_find.blocks and river_to_find.blocks[0] in river.blocks:
            return True

    return False


rivers = []


def search_next(river, matrix, row_index, col_index):
    if row_index >= len(matrix) or col_index >= len(matrix[row_index]):
        return

    item = matrix[row_index][col_index]
    river_block = RiverBlock(row_index, col_index)
    if not River.is_river_block(item):
        return

    if block_in_rivers(rivers, river_block):
        if river is None:
            return

        existing_river = get_river_of_block(rivers, river_block)
        existing_river.merge(river)
        return

    if river.is_block_in_river(river_block):
        return

    river.append(river_block)

    # search right
    search_next(river, matrix, row_index, col_index + 1)
    # search down
    search_next(river, matrix, row_index + 1, col_index)


for row_index, row in enumerate(matrix):
    for col_index, item in enumerate(row):
        if not River.is_river_block(item):
            continue

        river_block = RiverBlock(row_index, col_index)
        if block_in_rivers(rivers, river_block):
            continue

        river = River()
        river.append(river_block)

        search_next(river, matrix, row_index, col_index + 1)
        search_next(river, matrix, row_index + 1, col_index)
        if not is_river_in_rivers(river):
            rivers.append(river)


print(len(rivers))
for river in rivers:
    print(river)
