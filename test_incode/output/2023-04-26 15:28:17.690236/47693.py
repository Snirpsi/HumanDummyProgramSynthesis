#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or calculates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = ['hello', 'world', 'python', 'is', 'a', 'simple', 'webserver']
            
            print('\n'.join(words))
            
        elif sys.argv[1] == 'port':
            
            port = 8080
            
            print('Port: ' + str(port))
            
        else:
            
            print('Usage: python webserver.py words')
            
    else:
        
        print('Usage: python webserver.py words')
    
