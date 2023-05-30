#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1].split()
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    words = [str(word) for word in words]
    
    numbers = [str(i) for i in numbers]
    
    numbers_iter = iter(numbers)
    
    words_iter = iter(words)
    
    numbers_str = numbers_iter.next()
    
    words_str = words_iter.next()
    
    print('\n'.join(words))
    print('\n'.join(numbers))
    
    while True:
        try:
            number = int(numbers_str)
        except ValueError:
            print('Invalid number: %s' % numbers_str)
            continue
        
        try:
            word = next(words_iter)
        except StopIteration:
            print('No more words')
            break
        
        print('%s %s' % (word, number))
        
        numbers_str = numbers_iter.next()
        
        words_str = words_iter.next()
        
    print('\n'.join(words))
    print('\n'.join(numbers))
    
