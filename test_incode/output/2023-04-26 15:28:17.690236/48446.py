#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['foo', 'bar', 'baz']
    while True:
        print(' '.join(words))
        time.sleep(1)
        words = ['foo', 'bar', 'baz']

<|/ file source=github |>