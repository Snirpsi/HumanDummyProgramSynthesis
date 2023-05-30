#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or iterates over numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        
        for arg in sys.argv[1:]:
            words.append(arg)
        
        for word in words:
            print(word)
    else:
        for num in range(1, 101):
            print(num)
            
