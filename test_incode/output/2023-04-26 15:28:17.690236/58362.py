#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and calculates numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        
        words = words + arg.split(' ')
        
    for word in words:
        
        numbers.append(int(word))
        
    numbers = numbers + [sum(numbers[:i+1]) for i in range(len(numbers)-1)]
    
    print(' '.join(words))
    print(' '.join(numbers))
    
