#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and iterates over numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        webserver.serve_forever()
        
