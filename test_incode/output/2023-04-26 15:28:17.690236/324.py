#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    
    words = ['hello', 'world', '!']
    
    while True:
        
        for word in words:
            print(word)
            
        time.sleep(1)
    
