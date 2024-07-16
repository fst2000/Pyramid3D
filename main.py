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

def matrix(size : int): return enumerated_matrix(lambda i, j: 1 if i == j else 0, size)

def enumerated_matrix(function, size : int): return tuple(tuple(function(i, j) for j in range(size)) for i in range(size))

def map_matrix(function, matrix): return list(map(lambda row: list(map(lambda a: function(a), row)), matrix))

def transpose(m): return enumerated_matrix(lambda i, j: m[j[i]])

def column(matrix, idx : int): return list(map(lambda row: row[idx], matrix))

def dot_mat(m1, m2): return [dot_vec(row, column(m2, idx)) for idx, row in enumerate(m1)]

def y_rotation_matrix3(angle): return [
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