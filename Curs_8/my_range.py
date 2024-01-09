class PanaLa(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        val = self.current
        self.current += 1
        if self.current > self.end:
            raise StopIteration()
        return val

def my_range(end, start=0):
    return iter(PanaLa(start=start, end=end))