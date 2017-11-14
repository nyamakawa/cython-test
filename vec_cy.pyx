import numpy as np
cimport numpy as np

def dot_py(a, b):
    if len(a) != len(b):
        raise ValueError("Vector a and b should be same dimention")
    return sum([a[i] * b[i] for i in range(len(a))])

def dot_np(a, b):
    if len(a) != len(b):
        raise ValueError("Vector a and b should be same dimention")
    return np.dot(a, b)

def dot1(a, b):
    return dot1_imp(a, b)

def dot2(np.ndarray a, np.ndarray b):
    return dot2_imp(a, b)

def dot3(np.ndarray a, np.ndarray b):
    return dot3_imp(a, b)

cdef dot1_imp(object a, object b):
    cdef:
        int s = 0
        int len_a = len(a)

    if len(a) != len(b):
        raise ValueError("Vector a and b should be same dimention")
    for i in range(len_a):
        s += a[i] * b[i]    
    return s

cdef dot2_imp(np.ndarray a, np.ndarray b):
    cdef:
        int s = 0
        int len_a = len(a)
    if len(a) != len(b):
        raise ValueError("Vector a and b should be same dimention")
    for i in range(len_a):
        s += a[i] * b[i]    
    return s

cdef dot3_imp(np.ndarray a, np.ndarray b):
    cdef:
        int s = 0
        int len_a = len(a)
        int loops = int(len_a / 4)
        int offset = loops * 4
        int index

    if len(a) != len(b):
        raise ValueError("Vector a and b should be same dimention")
    for i in range(loops) :
        s += a[i] * b[i] + a[i+1] * b[i+1] + a[i+2] * b[i+2] + a[i+3] * b[i+3]
    for i in range(len_a % 4):
        index = offset+i
        s += a[index] * b[index] 

    return s
