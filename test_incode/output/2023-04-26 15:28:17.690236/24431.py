#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    words = []
    with open('words.txt') as f:
        words = f.readlines()
    
    words = [word.strip() for word in words]
    
    words = list(set(words))
    
    words.sort()
    
    with open('words.txt', 'w') as f:
        f.write('\n'.join(words))
    
    print('Done!')
    
