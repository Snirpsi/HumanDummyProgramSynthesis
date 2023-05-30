#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['foo', 'bar', 'baz']
    for index, word in enumerate(words):
        print('Word:', word, 'Index:', index)
        time.sleep(1)
