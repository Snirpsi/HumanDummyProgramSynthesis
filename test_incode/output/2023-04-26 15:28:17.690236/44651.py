#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        words.extend(['cat', 'dog', 'mouse'])
        
        print(' '.join(words))
        
        time.sleep(1)
