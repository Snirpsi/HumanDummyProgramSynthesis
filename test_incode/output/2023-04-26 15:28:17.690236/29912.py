#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'today', '?']
    
    while True:
        words.extend(['hello', 'world', 'how', 'are', 'you', 'today', '?'])
        
        print('\n'.join(' '.join(word) for word in words))
        
        time.sleep(1)
        
