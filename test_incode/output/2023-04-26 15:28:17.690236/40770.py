#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = []
        
        for arg in sys.argv[1:]:
            
            words = words + arg.split(' ')
        
        numbers = []
        
        for word in words:
            
            numbers.append(int(word))
        
        print(numbers)
        
    else:
        
        print('Usage: python webserver.py <words>')
        
