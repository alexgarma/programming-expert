def generate_string(string, frequency):
    position = 0
    while position < len(string):
        yield string[position] * frequency
        position += 1


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency
        self.position = 0

    def __iter__(self):
        self.position = 0
        return self
    
    def __next__(self):
        if self.position >= len(self.string):
            raise StopIteration

        char = self.string[self.position] * self.frequency
        self.position += 1
        return char