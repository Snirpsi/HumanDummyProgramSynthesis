#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        for word in words:
            print(word)
            
    else:
        
        print("Usage: %s <words>" % sys.argv[0])
        
