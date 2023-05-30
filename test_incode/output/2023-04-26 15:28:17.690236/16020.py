#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or iterates over all ports. """    
    
    ports = range(5000, 5999)
    
    server = HTTPServer(('', 5000), MyHandler)
    
    for port in ports:
        server.