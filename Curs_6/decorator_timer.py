import time

def timer(func):
    print("In decorator")
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print(f"A durat {end_time-start_time}")
        return value
    return wrapper

@timer
def dureaza_mult():
    raise Exception()
    time.sleep(10)

dureaza_mult()