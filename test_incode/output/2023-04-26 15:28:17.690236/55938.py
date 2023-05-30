#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['cat', 'dog', 'mouse', 'lion', 'sheep', 'cow']
    
    while True:
        words.pop(0)
        
        print(' '.join(words))
        
        time.sleep(1)
        
