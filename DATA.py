# constants(unit)
BLOCK_SIZE = 25 #(px)
FIELD_WIDTH = 10 #(blocks)
FIELD_HEIGHT = 24 #(blocks)
MOVEMENT = [
    [-1, 0],
    [0, 1],
    [1, 0]
]
LEFT = 0
DOWN = 1
RIGHT = 2

# TETRIMINO shape data
T = (
    [
        [0,1,0],
        [1,1,1],
        [0,0,0],
        [0,0,0]
    ],
    "medium purple"
    )

S = (
    [
        [0,1,1],
        [1,1,0],
        [0,0,0],
        [0,0,0]
    ],
    "green yellow"
    )

Z = (
    [
        [1,1,0],
        [0,1,1],
        [0,0,0],
        [0,0,0]
    ],
    "red"
    )

I = (
    [
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ],
    "cyan"
    )

J = (
    [
        [0,1,0],
        [0,1,0],
        [1,1,0],
        [0,0,0]
    ],
    "blue"
    )

L = (
    [
        [0,1,0],
        [0,1,0],
        [0,1,1],
        [0,0,0]
    ],
    "orange"
    )

O = (
    [
        [1,1,0],
        [1,1,0],
        [0,0,0],
        [0,0,0]
    ],
    "yellow"
    )

TETRIMINOS = [T, S, Z, I, J, L, O]