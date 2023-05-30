#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    while True:
        words = words + get_word()
        print(words)
        time.sleep(1)
    
