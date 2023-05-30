#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or multiplyes fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        for word in words:
            
            print(word*2)
            
    else:
        
        print("Usage: %s <words>" % sys.argv[0])
        
