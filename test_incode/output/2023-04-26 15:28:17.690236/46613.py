#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    
    words = []
    
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    words = list(set(words))
    
    words.sort()
    
    with open('words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')
            
    print('Done!')
    
