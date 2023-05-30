#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits or enumerates a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        fruit = sys.argv[1]
    else:
        fruit = 'apple'
    
    words = []
    
    for word in enumerate(fruit):
        words.append(word)
    
    print('\n'.join(map(str, words)))
    
