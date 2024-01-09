import time

class Timer():

    def __enter__(self):
        self.starttime = time.time()
    
    def __exit__(self, *args, **kwargs):
        self.stoptime = time.time()
        self.timptrecut = self.stoptime - self.starttime
        print(self.timptrecut)
        
        
with Timer():
    raise ValueError()
    time.sleep(5)