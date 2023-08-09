def get_n_longest_unique_words(words, n):
    
    counts = {

    }

    for word in words:
        counts[word] = counts.get(word,0) + 1
    unique_words_dict = counts.copy()
    for key, value in counts.items():
        if value > 1:
            del unique_words_dict[key]
        else:
            continue

    unique_words_lst = list(unique_words_dict.keys())
    unique_words_with_lengths = {}

    for word in unique_words_lst:
        unique_words_with_lengths[word] = len(word)
    top_n_words = sorted(unique_words_with_lengths,key = unique_words_with_lengths.get,reverse = True)
    top_n_words = top_n_words[:n]

    return top_n_words