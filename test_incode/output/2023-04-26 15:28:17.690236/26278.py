#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or prints a port. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(i)
        
    print('\n'.join(words))
    
