#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'convert':
            
            converter = Convert()
            converter.convert(sys.argv[2])
            
        elif sys.argv[1] == 'number':
            
            converter = Number()
            converter.convert(sys.argv[2])
            
        elif sys.argv[1] == 'word':
            
            converter = Word()
            converter.convert(sys.argv[2])
            
        else:
            
            print("Usage: python webserver.py <command>")
            
    else:
        
        print("Usage: python webserver.py <command>")
        
