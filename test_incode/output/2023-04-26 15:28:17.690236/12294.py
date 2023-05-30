#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['foo', 'bar', 'baz', 'qux']
    
    while True:
        words.remove(words.pop(0))
        
        print('Removed words: ', words)
        
        if words:
            print('Pausing for 5 seconds...')
            time.sleep(5)
            
