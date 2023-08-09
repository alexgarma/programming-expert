# TODO: Generar un offset aleatorio para descifar el mensaje (es decir, generar aleatoriamente su llave)
def caesar_cipher(string, offset):
    new_string = ""
    for char in string:
        if ord(char) - offset >= ord("a"):
            new_char = chr(ord(char) - offset)
            new_string += new_char
        else:
            steps_without_shift = ord(char) - ord("a")
            steps_with_shift = offset - steps_without_shift
            new_char = chr(ord("z") - (steps_with_shift - 1))
            new_string += new_char
    return new_string