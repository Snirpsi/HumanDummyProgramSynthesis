#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and multiplyes user input. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        words.append(line)
        
        if len(words) == 2:
            break
    
    words.sort()
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print('The product of the words is %s' % multiplier)
    
