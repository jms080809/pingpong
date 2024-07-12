from vpython import *
import random
import os
import chime

# Dimensions : kg,m,m/s,kg*m/s,kg*m/s^2

# setup - environment
scene.ambient = color.white * 0.7
container_pos = vec(0, 0, 0)

axis_size = 40  # m

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

scene.camera.pos = container_pos + vec(axis_size / 2, 0, axis_size / 2)


def try_init():
    # plate settings
    global plate_width
    plate_width = 10

    global plate_height
    plate_height = 2
    global plate
    plate = box(
        pos=container_pos + vec(axis_size / 2, -axis_size + 10, 0),
        size=vec(plate_width, plate_height, 0),
        color=vec(1, 1, 1),
    )
    plate.plate_radius = plate_width / 2
    global prev_plate_pos
    prev_plate_pos = plate.pos.x

    # scene-objectives
    global ball
    ball = sphere(
        pos=container_pos + vec(axis_size / 2, axis_size / 2, 0),
        radius=1,
        color=vec(1, random.random(), random.random()),
    )
    ball.mass = 1  # kg
    ball.velocity = vec(0, 0, 0)
    ball.p = ball.mass * ball.velocity

    # main first state
    ball.velocity = vector(0.7, -1, 0)
    global dt
    dt = 0.5

    global RATE
    RATE = 60
    global Score
    Score = 0


# main loop
retry = True

try_init()
while retry:
    rate(RATE)
    #
    ball.p = ball.mass * ball.velocity
    # print(ball.p)
    # score functions
    Score += 1 / RATE * 2
    # plate movement limit
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
            ball.velocity.value[0] * -1,
            ball.velocity.value[1],
            ball.velocity.value[2],
        )
    if ball.pos.x <= wall_Left.pos.x:
        ball.velocity = vec(
            ball.velocity.value[0] * -1,
            ball.velocity.value[1],
            ball.velocity.value[2],
        )
    if ball.pos.y >= wall_Top.pos.y:
        ball.velocity = vec(
            ball.velocity.value[0],
            ball.velocity.value[1] * -1,
            ball.velocity.value[2],
        )
    # ball-plate collision
    if (
        # in the range of on the plate
        plate.pos.x - plate.plate_radius <= ball.pos.x
        and ball.pos.x <= plate.pos.x + plate.plate_radius
        # at the positon of y of the plate
        and plate.pos.y + plate_height / 2
        >= ball.pos.y
        >= plate.pos.y - plate_height / 2
    ):
        if ball.pos.x < plate.pos.x:
            ball.velocity = vec(
                ball.velocity.value[0] * -1,
                ball.velocity.value[1] * -1,
                ball.velocity.value[2],
            )
        else:
            ball.velocity = vec(
                ball.velocity.value[0],
                ball.velocity.value[1] * -1,
                ball.velocity.value[2],
            )
    # GAMEOVER logic
    if ball.pos.y == wall_Bottom.pos.y:
        ball.visible = False
        plate.visible = False
        del ball
        del plate
        message = text(
            text=f"GAME_OVER\nYour Score: {round(Score)}",
            pos=vec(wall_Right.pos.x / 2, wall_Right.pos.y / 2, 0),
            align="center",
            height=8,
            color=color.red,
        )
        print(f"GAME OVER\nYour Score: {Score}")
        continuebool = list(
            input("Retry? then  input any characters or to stop, blank:")
        )
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
