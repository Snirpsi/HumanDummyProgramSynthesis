#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['foo', 'bar', 'baz']
    while True:
        words.extend(['qux', 'quux', 'quuux'])
        print('\n'.join(words))
        time.sleep(1)
