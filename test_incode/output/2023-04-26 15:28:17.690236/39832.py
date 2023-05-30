#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or iterates over numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word|number> [<word|number>]" % sys.argv[0])
        sys.exit(0)
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == '-':
            continue
        
        if arg == 'word':
            words.append(arg)
        elif arg == 'number':
            numbers.append(arg)
        else:
            print("Usage: %s <word|number> [<word|number>]" % sys.argv[0])
            sys.exit(0)
    
    if len(words) == 0 or len(numbers) == 0:
        print("Usage: %s <word|number> [<word|number>]" % sys.argv[0])
        sys.exit(0)
    
    words.sort()
    numbers.sort()
    
    i = 0
    
    for word in words:
        i += 1
        
        if word == '-':
            continue
        
        if word == 'word':
            print(words[i])
        elif word == 'number':
            print(numbers[i])
        else:
            print("Usage: %s <word|number> [<word|number>]" % sys.argv[0])
            sys.exit(0)
    
