def new_range(start,stop,step):
    
    current = start
    
    if not (stop - start > 0 and step > 0) and not (stop - start < 0 and step < 0):
        return None

    while abs(current) < abs(stop):
        yield current
        current += step