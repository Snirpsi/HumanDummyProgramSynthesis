#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['foo', 'bar', 'baz']
    
    while True:
        
        words.pop()
        
        print(' '.join(words))
        
        time.sleep(1)
        
