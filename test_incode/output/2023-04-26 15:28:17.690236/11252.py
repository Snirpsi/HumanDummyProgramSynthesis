#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        if len(words) > 0:
            
            for word in words:
                
                print(word)
                
        else:
            
            print("Usage: %s <words>" % sys.argv[0])
            
    else:
        
        print("Usage: %s <words>" % sys.argv[0])
        
    
