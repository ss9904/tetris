# constants(unit)
BLOCK_SIZE = 25 #(px)
FIELD_WIDTH = 10 #(blocks)
FIELD_HEIGHT = 24 #(blocks)
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
    "medium purple"
    )

S = (
    [
        [0,1,1],
        [1,1,0],
    ],
    "green yellow"
    )

Z = (
    [
        [1,1,0],
        [0,1,1],
    ],
    "red"
    )

I = (
    [
        [1],
        [1],
        [1],
        [1]
    ],
    "cyan"
    )

J = (
    [
        [0,1],
        [0,1],
        [1,1]
    ],
    "blue"
    )

L = (
    [
        [1,0],
        [1,0],
        [1,1],
    ],
    "orange"
    )

O = (
    [
        [1,1],
        [1,1]
    ],
    "yellow"
    )

TETRIMINOS = [T, S, Z, I, J, L, O]