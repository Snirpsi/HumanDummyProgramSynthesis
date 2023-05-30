#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        
        if word in ['all', 'words']:
            
            for number in range(1, 100):
                
                print("%03d" % (number))
                
        else:
            
            print("%03d" % int(word))
            
    