#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and enumerates words. """    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == '--help':
            usage()
            sys.exit()
        elif arg == '--numbers':
            numbers = range(1,len(sys.argv))
        elif arg == '--words':
            words = sys.argv[1:]
        else:
            usage()
            sys.exit()
    
    numbers = list(numbers)
    words = list(words)
    
    numbers.sort()
    words.sort()
    
    for num in numbers:
        print('%d: %s' % (num, words[num-1]))
    
    for word in words:
        print('%s' % word)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
