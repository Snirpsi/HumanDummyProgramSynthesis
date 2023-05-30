#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or stores user input. """    
    while True:
        words = get_words()
        if words:
            print(words)
        else:
            break
