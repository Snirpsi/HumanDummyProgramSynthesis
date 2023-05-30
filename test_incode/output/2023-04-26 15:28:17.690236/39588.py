#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    while True:
        words = get_words()
        if words:
            open_word(words)
        else:
            print("No words found")
            
