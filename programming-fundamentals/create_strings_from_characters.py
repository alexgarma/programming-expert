""" TODO: Improve this previous solution. 

def create_strings_from_characters(frequencies, string1, string2):
    print(f"Length of the frequencies dict: {len(frequencies)}")
    if len(frequencies) == 0 and (len(string1) > 0 or len(string2)>0):
        return 0
    if len(frequencies) >= 0 and (len(string1) == 0 and len(string2) ==0):
        return 2
    
    counts_string1 = {}
    counts_string2 = {}

    for char in string1:
        counts_string1[char] = counts_string1.get(char,0) + 1
    for char in string2:
        counts_string2[char] = counts_string2.get(char,0) + 1

    validation1 = []
    validation2 = []
    validation3 = []

    for char,count in frequencies.items():
        print(f"---- Character to evaluate: {char} ----")
        print(f"Frequency: {count}")
        count_in_string1_required = counts_string1.get(char,0)
        print(f"Chars needed in string1: {count_in_string1_required}")
        count_in_string2_required = counts_string2.get(char,0)
        print(f"Chars needed in string2: {count_in_string2_required}")

        can_generate_both = True if count >= (count_in_string1_required + count_in_string2_required) else False
        can_generate_string1 = True if (can_generate_both == False) and (count >= count_in_string1_required) else False
        can_generate_string2 = True if (can_generate_both == False) and (count >= count_in_string2_required) else False

        if can_generate_both:
            validation1.append(1)
            validation2.append(1)
            validation3.append(0)
        elif can_generate_string1 or can_generate_string2:
            validation1.append(0)
            validation2.append(1)
            validation3.append(0)
        else:
            validation1.append(0)
            validation2.append(0)
            validation3.append(1)

    print(f"Validation 1 : {validation1}")
    print(f"Validation 2 : {validation2}")
    print(f"Validation 3 : {validation3}")
    if sum(validation1) == len(list(frequencies.keys())) :
        return 2
    elif sum(validation2) == len(list(frequencies.keys())) :
        return 1
    else:
        return 0
"""

def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = can_create_string_from_frequencies(
        frequencies, string1)
    can_create_string2 = can_create_string_from_frequencies(
        frequencies, string2)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1

        return 0

    for character in string1 + string2:
        if character not in frequencies or frequencies[character] == 0:
            return 1

        frequencies[character] -= 1

    return 2


def can_create_string_from_frequencies(frequencies, string):
    for character in set(string):
        if string.count(character) > frequencies.get(character, 0):
            return False

    return True