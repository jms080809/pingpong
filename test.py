from vpython import *
import tkinter as tk
import random

# a = sphere(pos=vec(0, 0, 0), size=vec(1, 1, 1), make_trail=True, color=vec(0, 1, 0))

# b = box(pos=vec(3, 2, 0), size=vec(1, 1, 1), color=vec(1, 0, 0))

# side = 8
# thk = 0.3
# s2 = 2 * side - thk
# s3 = 2 * side + thk

# wallR = box(pos=vector(side, 0, 0), size=vector(thk, s2, s3), colo1r=color.red)
# wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color=color.red)
# wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3), color=color.blue)
# wallT = box(pos=vector(0, side, 0), size=vector(s3, thk, s3), color=color.blue)
# wallBK = box(
#     pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7)
# )
# wallF = box(pos=vector(0, 0, side), size=vector(s2, s2, thk), opacity=0)

# velocity = vector(random() * 100, random() * 100, random() * 100)
# dt = 0.1
# compl = 1

# a.mass = 0
# ar = arrow(pos=a.pos, axis=b.pos - a.pos, color=color.green)

# while True:
#     plusminus = round(random()) if round(random()) == 1 else -round(random())
#     ar.pos = a.pos
#     ar.axis = (a.pos + velocity - a.pos) / 1
#     rate(100)
#     a.pos += velocity * dt
#     if a.pos.x >= wallR.pos.x - compl or a.pos.x - compl <= wallL.pos.x:
#         velocity.x *= -1  # +plusminus * random()
#     if a.pos.y >= wallT.pos.y - compl or a.pos.y + compl <= wallB.pos.y:
#         velocity.y *= -1  # +plusminus * random()
#     # print("%0.1f %0.1f"%(a.pos.x,a.pos.y))
#     if a.pos.z - compl >= wallF.pos.z or a.pos.z + compl <= wallBK.pos.z:
#         velocity.z *= -1  # +plusminus * random()
#     a.trail_color = vec(random(), random(), random())


# Setup - environment
scene.ambient = color.white * 0.7
container_pos = vec(0, 0, 0)

axis_size = 10  # m

wall_thin = 0.5
wall_Right = box(
    pos=container_pos + vec(axis_size * 2, 0, 0),
    color=vec(1, random.random(), random.random()),
    size=vec(wall_thin, axis_size * 2, 0),
)
wall_Left = box(
    pos=container_pos + vec(0, 0, 0),
    color=vec(1, random.random(), random.random()),
    size=vec(wall_thin, axis_size * 2, 0),
)
wall_Bottom = box(
    pos=container_pos + vec(wall_Right.pos.x / 2, -axis_size, 0),
    color=vec(1, random.random(), random.random()),
    size=vec(axis_size * 2, wall_thin, 0),
)
wall_Top = box(
    pos=container_pos + vec(wall_Right.pos.x / 2, axis_size, 0),
    color=vec(1, random.random(), random.random()),
    size=vec(axis_size * 2, wall_thin, 0),
)

# Number of blocks and row and column
N = 20
# Number of blocks' row and column
M = 9

# Block dimensions
block_width = (wall_Right.pos.x - wall_Left.pos.x) / N
block_height = (wall_Top.pos.y - wall_Bottom.pos.y) * 50 / 100 / M

# Create blocks
blocks = []
for j in range(M):
    for i in range(N):
        block = box(
            pos=container_pos
            + vec(
                wall_Left.pos.x + block_width / 2 + i * block_width,
                wall_Top.pos.y - 2 * wall_thin - j * block_height,
                0,
            ),
            size=vec(block_width, block_height, wall_thin),
            color=vec(random.random(), random.random(), random.random()),
        )
        blocks.append(block)


# Print the position of blocks (for verification)
for block in blocks:
    print(f"Block position: {block.pos.x}")


# Adjust the camera position to better view the blocks


a = [1, 2, 3]
for i in a:
    a[a.index(i)] = None
    del i
    print(a)
