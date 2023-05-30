#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    i = 0
    
    for word in words:
        print(words[i], end='')
        i += 1
        
        if i == len(words):
            break
        
        words[i] = word.capitalize()
        
    print('')
    
