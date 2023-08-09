class Range:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        
        if self.current >= self.stop:
            raise StopIteration
        
        num = self.current
        self.current += self.step

        return num