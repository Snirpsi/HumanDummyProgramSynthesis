#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or stores a list of numbers. """    
    port = 0
    numbers = []
    
    try:
        port = int(sys.argv[1])
    except:
        pass
    
    try:
        numbers = sys.argv[2:]
    except:
        pass
    
    numbers = map(int, numbers)
    
    if port == 0:
        port = 9999
    
    httpd = make_server('', port, handle_request)
    httpd.serve_forever()
    
