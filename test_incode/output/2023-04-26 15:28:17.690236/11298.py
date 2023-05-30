#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and multiplyes fruits. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words.sort()
    
    fruits = [0] * len(words)
    
    for index, word in enumerate(words):
        fruits[index] = word
    
    for index, word in enumerate(fruits):
        fruits[index] = word * 2
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate(fruits):
        print(word, end=' ')
    
    print('')
    
    for index, word in enumerate