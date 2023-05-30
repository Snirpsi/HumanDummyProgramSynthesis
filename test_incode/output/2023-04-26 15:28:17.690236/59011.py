#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or opens words. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        exit(1)
    
    webserver = WebServer()
    webserver.run(port)
    
