#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        print('\n'.join(words))
        
        time.sleep(1)
        
        words.append('cat')
        
        time.sleep(1)
        
        words.append('dog')
        
        time.sleep(1)
        
        words.append('mouse')
        
        time.sleep(1)
        
