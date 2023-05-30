#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or opens a port. """    
    
    # Open a port if port is given
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        # Open a port if word is given
        if len(sys.argv) > 2:
            word = int(sys.argv[2])
            
            open_port(port, word)
    
    else:
        open_port()
    
