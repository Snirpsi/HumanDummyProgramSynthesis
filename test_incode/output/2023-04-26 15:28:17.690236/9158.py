#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or enumerates numbers. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        
        if arg == '--words':
            
            words = list(set(sys.argv[2:]))
            
        elif arg == '--numbers':
            
            numbers = list(set(sys.argv[2:]))
            
        else:
            
            words.append(arg)
            
    words.sort()
    
    for word in words:
        
        print(word, end=' ')
        
    for number in numbers:
        
        print(number, end=' ')
        
    print('')
    
