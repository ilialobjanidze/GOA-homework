#1
def potatoes(p0, w0, p1):
    w1 = (w0 * (1 - p0 / 100)) / (1 - p1 / 100)
    return int(w1)



