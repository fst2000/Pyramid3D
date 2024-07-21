import math
from functools import reduce
from operator import mul
import glfw
from OpenGL.GL import *

def length(vec): return math.sqrt(sum(map(lambda i: i * i), vec))

def angle(v1, v2): return math.acos(dot_vec(v1, v2) / length(v1) * length(v2))

def dot_vec(v1, v2): return sum(map(lambda a1, a2: a1 * a2, v1, v2))

def cross(v1, v2): pass

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

def transform_face(matrix, face): return tuple(map(lambda v: dot_mat_vec(matrix, v), face))

def transform_mesh(matrix, mesh): return tuple(map(lambda f: transform_face(matrix, f), mesh))

def draw_face(face):
    for vec in face:
        glColor3f(*vec)
        glVertex(*vec)

def normal(face):
    return

def draw(mesh):
    glBegin(GL_TRIANGLES)
    for face in mesh: draw_face(face)
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
    angle = 0.0
    pyramid_mesh = (((0, 0.5, 0), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5)),
                     ((0, 0.5, 0), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)),
                     ((0, 0.5, 0), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5)),
                     ((0, 0.5, 0), (-0.5, -0.5, 0.5), (-0.5, -0.5, 0.5)))
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        draw(transform_mesh(y_rot_mat(angle), pyramid_mesh))
        angle += 0.001
        glfw.swap_buffers(window)
    glfw.terminate()

main()