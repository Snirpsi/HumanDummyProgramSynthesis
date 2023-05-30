#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        print('\n'.join(words))
        
        time.sleep(1)
        
        words.append('cat')
        words.append('dog')
        words.append('mouse')
        
