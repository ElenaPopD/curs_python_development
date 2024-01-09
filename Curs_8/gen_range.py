def gen_range(end, start=0):
    current = start
    while current < end:
        yield current
        current += 1