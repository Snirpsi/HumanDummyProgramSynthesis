#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or enumerates a list of words. """    
    
    import sys
    
    numbers = []
    words = []
    
    for arg in sys.argv[1:]:
        
        if arg == '-numbers':
            numbers = sys.argv[2:]
            
        elif arg == '-words':
            words = sys.argv[2:]
            
        else:
            print('Usage: %s [-numbers] [-words] <numbers>' % sys.argv[0])
            
            sys.exit(1)
            
    if len(numbers) == 0:
        print('Usage: %s [-numbers] [-words] <numbers>' % sys.argv[0])
        
        sys.exit(1)
        
    if len(words) == 0:
        print('Usage: %s [-numbers] [-words] <numbers>' % sys.argv[0])
        
        sys.exit(1)
    
    if len(numbers) != len(words):
        print('Usage: %s [-numbers] [-words] <numbers>' % sys.argv[0])
        
        sys.exit(1)
    
    numbers = list(map(int, numbers))
    words = list(map(str, words))
    
    numbers.sort()
    words.sort()
    
    numbers_str = ','.join(str(x) for x in numbers)
    words_str = ','.join(str(x) for x in words)
    
    print('Numbers: %s' % numbers_str)
    print('Words: %s' % words_str)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
