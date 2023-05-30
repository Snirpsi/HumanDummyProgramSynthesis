#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s <word|number> ..." % sys.argv[0])
        sys.exit()
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == 'word':
            words.append(1)
        elif arg == 'number':
            numbers.append(1)
        else:
            print("Usage: %s <word|number> ..." % sys.argv[0])
            sys.exit()
    
    numbers = numbers[:]
    
    i = 0
    while i < len(words):
        word = words[i]
        number = numbers[i]
        
        if word == 1:
            words[i] = number
        elif word == 0:
            numbers[i] = number
        else:
            print("Usage: %s <word|number> ..." % sys.argv[0])
            sys.exit()
        
        i += 1
    
    print("\n".join(words))
    print("\n".join(numbers))
    
