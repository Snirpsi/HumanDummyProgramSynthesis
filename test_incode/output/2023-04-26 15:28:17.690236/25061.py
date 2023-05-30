#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and iterates over a port. """    
    
    port = 5000
    
    while True:
        
        words = []
        
        for i in range(10):
            words.append('word')
        
        print('\n'.join(words))
        
        time.sleep(1)
        
