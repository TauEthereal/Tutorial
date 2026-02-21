def stats(stat):
    import math
    a = math.floor(stat/20)
    b = math.ceil(stat/40)
    c = stat%20
    if c == 0:
        d = 0
    elif 0.001 <= c <= 0.499:
        d = 2
    elif 0.5 <= c <= 0.749:
        d = 4
    else:
        d = 6
    return print("{a}к10"+"{b+d}")

    