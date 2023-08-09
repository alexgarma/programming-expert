def filter_integers(func):
    def wrapper(*args):
        ints = [x for x in args if isinstance(x,int)]
        print(f"Filtered ints: {ints}")
        return func(*ints)
        
    return wrapper

def convert_strings_to_ints(func):
    def wrapper(*args):
        parsed = []
        for x in args:
            if isinstance(x,str):
                if x.isdigit():
                    parsed.append(int(x))
                elif x[0] == "-" and x[1:].isdigit():
                    parsed.append(int(x))
            else:
                parsed.append(x)
        print(f"Converted to ints: {parsed}")
        return func(*parsed)
        
    return wrapper

def flatten_lists(func):
    def wrapper(*args):
        flatten = []
        for arg in args:
            if isinstance(arg,list):
                flatten.extend(arg)
            else:
                flatten.append(arg)
        print(f"Flatten args: {flatten}")
        return func(*flatten)
    
    return wrapper

@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)