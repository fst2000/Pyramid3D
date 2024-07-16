import math
from functools import reduce
from operator import mul
import glfw
from OpenGL.GL import *

def length(vec): return math.sqrt(sum(map(lambda i: i * i), vec))

def angle(v1, v2): return math.acos(dot_vec(v1, v2) / length(v1) * length(v2))

def dot_vec(v1, v2): return sum(map(lambda a1, a2: a1 * a2, v1, v2))

def matrix(size : int): return enumerated_matrix(lambda i, j: 1 if i == j else 0, size)

def enumerated_matrix(function, size : int): return tuple(tuple(function(i, j) for j in range(size)) for i in range(size))

def map_matrix(function, matrix): return tuple(map(lambda row: tuple(map(lambda a: function(a), row)), matrix))

def transpose(m): return enumerated_matrix(lambda i, j: m[j[i]])

def column(matrix, idx : int): return tuple(map(lambda row: row[idx], matrix))

def dot_mat(m1, m2): return tuple(enumerated_matrix(lambda i, j: dot_vec(m1[i], column(m2, j)), len(m1)))

def dot_mat_vec(m, v): return tuple(dot_vec(row, v) for row in m)

def y_rot_mat(angle): return [
    [math.cos(angle), 0, math.sin(angle)],
    [0, 1, 0],
    [-math.sin(angle), 0, math.cos(angle)]
    ]

def draw(angle : float):
    glBegin(GL_TRIANGLES)
    vecs = ((0, 0.5, 0), (0.5, -0.5, 0), (-0.5, -0.5, 0))
    rot_mat = y_rot_mat(angle)
    for vec in map(lambda vec: dot_mat_vec(rot_mat, vec), vecs): glVertex(*vec)
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
    angle = 30.0
    while not glfw.window_should_close(window):
        glfw.poll_events()
        draw(angle)
        angle += 0.01
        glfw.swap_buffers(window)
    glfw.terminate()

main()