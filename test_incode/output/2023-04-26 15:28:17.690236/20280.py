#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    
    words = ['a', 'b', 'c']
    
    while True:
        
        words.pop()
        
        print('Removed {}'.format(words))
        
        time.sleep(1)
        
