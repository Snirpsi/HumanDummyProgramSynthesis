#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['foo', 'bar', 'baz']
    while True:
        for word in words:
            print(word)
        time.sleep(1)
