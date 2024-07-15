import math
from functools import reduce
from operator import mul
import glfw
from OpenGL.GL import *

def vec2(x, y): return {"x": x, "y": y}

def vec3(x, y, z): return {"x": x, "y": y, "z": z}

def length(vec): return math.sqrt(sum(map(lambda i: i * i), vec.values()))

def angle(v1, v2): return math.acos(dot_vec(v1, v2) / length(v1) * length(v2))

def dot_vec(v1, v2): return sum(map(lambda a1, a2: a1 * a2, v1.values(), v2.values()))

def matrix4(): return list(map(lambda i: list(map(lambda j: 1 if i == j else 0, range(4))), range(4)))

def transpose(mat, size): return list(map(lambda a, i: a, mat, range(reduce(mul, size))))

def dot_mat4(m1, m2): pass

def y_rotation_matrix3(angle):
    return [
    [math.cos(angle), 0, math.sin(angle)],
    [0, 1, 0],
    [-math.sin(angle), 0, math.cos(angle)]
    ]

def draw():
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(-0.5, -0.5, 0)
    glEnd()

def start_window():
    window = glfw.create_window(1000, 1000, "draw_test", None, None)
    glfw.make_context_current(window)
    if not window:
        glfw.terminate()
        print("Glfw window can't be created")
        exit()
    return window

def main():
    glfw.init()
    window = start_window()
    while not glfw.window_should_close(window):
        glfw.poll_events()
        draw()
        glfw.swap_buffers(window)
    glfw.terminate()

main()