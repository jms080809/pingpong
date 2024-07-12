from vpython import *
import random
import os
import chime
import time

# Dimensions : kg,m,m/s,kg*m/s,kg*m/s^2

# setup - environment
scene.ambient = color.white * 0.7
container_pos = vec(
    0,
    0,
    0,
)

axis_size = 40  # m

wall_thin = 0.5
wall_Right = box(
    pos=container_pos
    + vec(
        axis_size * 2,
        0,
        0,
    ),
    color=vec(
        1,
        random.random(),
        random.random(),
    ),
    size=vec(
        wall_thin,
        axis_size * 2,
        0,
    ),
)
wall_Left = box(
    pos=container_pos
    + vec(
        0,
        0,
        0,
    ),
    color=vec(
        1,
        random.random(),
        random.random(),
    ),
    size=vec(
        wall_thin,
        axis_size * 2,
        0,
    ),
)
wall_Bottom = box(
    pos=container_pos
    + vec(
        wall_Right.pos.x / 2,
        -axis_size,
        0,
    ),
    color=vec(
        1,
        random.random(),
        random.random(),
    ),
    size=vec(
        axis_size * 2,
        wall_thin,
        0,
    ),
)
wall_Top = box(
    pos=container_pos
    + vec(
        wall_Right.pos.x / 2,
        axis_size,
        0,
    ),
    color=vec(
        1,
        random.random(),
        random.random(),
    ),
    size=vec(
        axis_size * 2,
        wall_thin,
        0,
    ),
)

scene.camera.pos = container_pos + vec(
    wall_Right.pos.x / 2,
    0,
    0,
)


def try_init():
    # plate settings
    global plate_width
    plate_width = 10

    global plate_height
    plate_height = 2
    global plate
    plate = box(
        pos=container_pos
        + vec(
            axis_size / 2,
            -axis_size + 10,
            0,
        ),
        size=vec(
            plate_width,
            plate_height,
            0,
        ),
        color=vec(
            1,
            1,
            1,
        ),
    )
    plate.plate_radius = plate_width / 2
    global prev_plate_pos
    prev_plate_pos = plate.pos.x

    # scene-objectives
    global ball
    ball = sphere(
        pos=container_pos
        + vec(
            axis_size / 2,
            0,
            0,
        ),
        radius=1,
        color=vec(
            1,
            random.random(),
            random.random(),
        ),
    )
    ball.mass = 1  # kg
    ball.velocity = vec(
        0,
        0,
        0,
    )
    ball.p = ball.mass * ball.velocity

    # main first state
    ball.velocity = vector(
        0.7,
        -1,
        0,
    )
    global dt
    dt = 0.5

    # obstacle blocks generation

    # Number of blocks and row and column
    N = 10
    # Number of blocks' row and column
    M = 5

    # Block dimensions
    global block_width
    block_width = (wall_Right.pos.x - wall_Left.pos.x) / N
    global block_height
    block_height = (wall_Top.pos.y - wall_Bottom.pos.y) * 50 / 100 / M

    # Create blocks
    global blocks
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
                size=vec(
                    block_width,
                    block_height,
                    wall_thin,
                ),
                color=vec(
                    random.random(),
                    random.random(),
                    random.random(),
                ),
            )
            blocks.append(block)
    ready_message = text(
        text=f"Get Ready!\nWill be started in 3 seconds",
        pos=vec(
            wall_Right.pos.x / 2,
            wall_Right.pos.y / 2,
            0,
        ),
        align="center",
        height=8,
        color=color.blue,
    )
    time.sleep(3)
    ready_message.visible = False
    del ready_message


# wowsexy
global RATE
RATE = 60
global Score
Score = 0


# def block_detect():
#     def _delblock(block):
#         block.visible = False
#         blocks[blocks.index(block)] = None
#         del block
# for block in blocks:
#     if blocks[blocks.index(block)] is None:
#         break
#     if (
#         ball.pos.x - ball.radius <= block.pos.x + block_width / 2
#         or ball.pos.x + ball.radius >= block.pos.x - block_width / 2
#     ):
#         _delblock(block)
#         ball.velocity.x *= -1
#     if (
#         ball.pos.y + ball.radius >= block.pos.y - block_width / 2
#         or ball.pos.y - ball.radius <= block.pos.y + block_width / 2
#     ):
#         _delblock(block)
#         ball.velocity.y *= -1
#     break


def block_detect():
    def _delblock(
        block,
    ):
        block.visible = False
        blocks[blocks.index(block)] = None
        del block

    for block in blocks:
        if block is None:
            continue

        # Check for collision with the sides of the block
        if (
            ball.pos.x + ball.radius >= block.pos.x - block.size.x / 2
            and ball.pos.x - ball.radius <= block.pos.x + block.size.x / 2
            and ball.pos.y + ball.radius >= block.pos.y - block.size.y / 2
            and ball.pos.y - ball.radius <= block.pos.y + block.size.y / 2
        ):
            # Determine the side of the collision and reflect ball accordingly
            if ball.pos.x < block.pos.x - block.size.x / 2 or ball.pos.x > block.pos.x + block.size.x / 2:
                ball.velocity.x *= -1
            else:
                ball.velocity.y *= -1
            _delblock(block)
            global Score
            Score += 1
            break  # Exit the loop after handling the collision to avoid multiple deletions


# main loop
retry = True
try_init()

while retry:
    rate(RATE)
    #
    # ball.p = ball.mass * ball.velocity
    # print(ball.p)
    # score functions
    # plate movement & plate movement limit
    plate.pos.x = scene.mouse.pos.x
    if plate.pos.x >= wall_Right.pos.x - plate.plate_radius / 2:
        plate.pos.x = wall_Right.pos.x - plate.plate_radius / 2
    if plate.pos.x <= wall_Left.pos.x + plate.plate_radius / 2:
        plate.pos.x = wall_Left.pos.x + plate.plate_radius / 2

    # ball moving
    ball.pos += ball.velocity * dt
    # ball-objects collisions
    # ball-wall collision
    if ball.pos.x >= wall_Right.pos.x:
        ball.velocity = vec(
            ball.velocity.x * -1,
            ball.velocity.y,
            ball.velocity.z,
        )
    if ball.pos.x <= wall_Left.pos.x:
        ball.velocity = vec(
            ball.velocity.x * -1,
            ball.velocity.y,
            ball.velocity.z,
        )
    if ball.pos.y >= wall_Top.pos.y:
        ball.velocity = vec(
            ball.velocity.x,
            ball.velocity.y * -1,
            ball.velocity.z,
        )
    # ball-plate collision
    if (
        # in the range of on the plate
        plate.pos.x - plate.plate_radius <= ball.pos.x
        and ball.pos.x <= plate.pos.x + plate.plate_radius
        # at the positon of y of the plate
        and plate.pos.y + plate_height / 2 >= ball.pos.y >= plate.pos.y - plate_height / 2
    ):
        ball.velocity.y *= -1

    # ball-blocks collision
    block_detect()
    # GAME WIN logic
    if Score == len(blocks):
        message = text(
            text=f"YOU WON!\nYour Score: {round(Score)}",
            pos=vec(
                wall_Right.pos.x / 2,
                wall_Right.pos.y / 2,
                0,
            ),
            align="center",
            height=8,
            color=color.red,
        )
        print(f"YOU WON!\nYour Score: {Score}")
        continuebool = list(input("Retry? then  input any characters or to stop, blank:"))
        print(len(continuebool))
        chime.success()

        if len(continuebool) != 0:
            message.visible = False
            del message
            try_init()
            continue
        else:
            retry = False
            break
    # GAMEOVER logic
    if ball.pos.y <= wall_Bottom.pos.y:
        ball.visible = False
        plate.visible = False
        del ball
        del plate
        message = text(
            text=f"GAME_OVER\nYour Score: {round(Score)}",
            pos=vec(
                wall_Right.pos.x / 2,
                wall_Right.pos.y / 2,
                0,
            ),
            align="center",
            height=8,
            color=color.red,
        )
        print(f"GAME OVER\nYour Score: {Score}")
        continuebool = list(input("Retry? then  input any characters or to stop, blank:"))
        print(len(continuebool))
        chime.success()

        if len(continuebool) != 0:
            message.visible = False
            del message
            try_init()
            continue
        else:
            retry = False
            break
os._exit(1972)
