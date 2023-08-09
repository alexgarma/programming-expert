def positive_even_squares(*args):
    
    positive_even_nums = list(map(lambda lst : list(filter(lambda x: x % 2 == 0 and x > 0,lst)),args))
    
    combined = []
    for element in positive_even_nums:
        combined.extend(element)
    
    return list(map(lambda x : x ** 2, combined))

args = [[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]

print(positive_even_squares(*args))