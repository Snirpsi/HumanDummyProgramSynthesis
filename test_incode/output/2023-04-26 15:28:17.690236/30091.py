#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or enumerates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0:
            
            words = []
            
            for word in sys.argv[2:]:
                
                words.append(word)
                
            words = ' '.join(words)
            
            print(words * port)
            
        else:
            
            print("Usage: python %s <port>" % sys.argv[0])
            
    else:
        
        print("Usage: python %s <port>" % sys.argv[0])
        
