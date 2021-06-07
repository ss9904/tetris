# constants(unit)
BLOCK_SIZE = 25 #(px)
FIELD_WIDTH = 10 #(blocks)
FIELD_HEIGHT = 20 #(blocks)
CENTER = int(FIELD_WIDTH/2)-1

MOVEMENT = [
    [1, 0],
    [0, 1],
    [-1, 0]
]
RIGHT = 0
DOWN = 1
LEFT = 2

# TETRIMINO shape data
T = (
    [
        [0,1,0],
        [1,1,1],
    ],
    1
    )

S = (
    [
        [0,1,1],
        [1,1,0],
    ],
    2
    )

Z = (
    [
        [1,1,0],
        [0,1,1],
    ],
    3
    )

I = (
    [
        [1],
        [1],
        [1],
        [1]
    ],
    4
    )

J = (
    [
        [0,1],
        [0,1],
        [1,1]
    ],
    5
    )

L = (
    [
        [1,0],
        [1,0],
        [1,1],
    ],
    6
    )

O = (
    [
        [1,1],
        [1,1]
    ],
    7
    )

TETRIMINOS = [T, S, Z, I, J, L, O]
COLORS = [
    "gray70",
    "medium purple",
    "green yellow",
    "red",
    "cyan",
    "blue",
    "orange",
    "yellow"
]