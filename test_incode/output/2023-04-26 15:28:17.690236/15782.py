#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        words.append('cat')
        words.append('dog')
        words.append('mouse')
        
        print(' '.join(words))
        
        time.sleep(1)
        
