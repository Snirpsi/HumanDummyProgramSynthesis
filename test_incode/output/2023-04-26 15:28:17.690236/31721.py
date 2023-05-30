#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    
    i = 0
    while True:
        i += 1
        print('Word', i, 'is', words[i])
        
        if i == len(words):
            break
            
        words[i] = words[i] + '