#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words and converts a list of words. """    
    words = word_list(sys.argv[1])
    words_converted = convert_words(words)
    print(words_converted)

<|/ file source=github ext=.py |>