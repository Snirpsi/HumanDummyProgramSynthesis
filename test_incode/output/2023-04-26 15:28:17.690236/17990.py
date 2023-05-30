#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or prints all ports. """    
    port = int(sys.argv[1])
    
    if port > 0:
        webserver.run(port)
    else:
        print('No port specified')
    
