#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and stores a port. """    
    words = ['foo', 'bar', 'baz']
    
    while True:
        for word in words:
            print(word)
            
        time.sleep(1)
    
