#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = []
        
        for arg in sys.argv[1:]:
            
            words = words + arg.split()
            
        words = list(set(words))
        
        words.sort()
        
        for word in words:
            
            print(word, end=" ")
            
        
    else:
        
        print("Usage: python word