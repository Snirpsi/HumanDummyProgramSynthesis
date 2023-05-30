#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and calculates words. """    
    words = []
    for word in word_list:
        words.append(word)
    words = list(set(words))
    words.sort()
    return words

<|/ file filename=word_list.py source=github |>