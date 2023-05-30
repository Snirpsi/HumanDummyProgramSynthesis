#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'today', '?']
    
    while True:
        for word in words:
            print(word)
        
        print('Press ENTER to exit.')
        
        