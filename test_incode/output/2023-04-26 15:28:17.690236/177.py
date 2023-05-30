#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or returns numbers. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        words = ['word1', 'word2', 'word3']
    
    numbers = []
    
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    
    if len(numbers) == 0:
        numbers = [1, 2, 3, 4]
    
    numbers = list(map(int, numbers))
    
    numbers = zip(numbers, words)
    
    for number, word in numbers:
        print('%s: %s' % (number, word))
    
