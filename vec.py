def dot(a, b):
    if len(a) != len(b):
        raise ValueError("Vector dimention is not equal")
    return sum([a[i] * b[i] for i in range(len(a))])

def dot_np(a, b):
    if len(a) != len(b):
        raise ValueError("Vector a and b should be same dimention")
    return a * b