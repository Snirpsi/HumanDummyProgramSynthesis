#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['foo', 'bar', 'baz', 'qux', 'quux', 'quuux', 'quuuuux']
    
    while True:
        for word in words:
            print(word)
        
        print('