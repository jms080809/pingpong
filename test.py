from vpython import *
import tkinter as tk

print(vec(tuple([1, 1, 1])))

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
