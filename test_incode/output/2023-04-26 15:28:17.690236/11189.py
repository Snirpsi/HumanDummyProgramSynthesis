#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    while True:
        words = read_words()
        if words:
            for word in words:
                print(word)
        else:
            break
