#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or returns all ports. """    
    
    ports = []
    
    try:
        ports = [int(port) for port in sys.argv[1:]]
    except:
        pass
    
    if len(ports) == 0:
        ports = [8000]
    
    for port in ports:
        
        server = HTTPServer(('', port), MyHandler)
        server.serve_forever()
        
    print('Listening on port ' + str(port))
    
