#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while True:
        print(' '.join(words))
        time.sleep(1)
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
