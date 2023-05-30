#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or calculates user input. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        webserver.serve_forever()
    elif port == 8081:
        webserver.serve_forever(use_debugger=True)
    else:
        webserver.serve_forever(use_debugger=False, port=port)
        
