#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    
    ports = [8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009]
    
    server = HTTPServer(('', 8000), MyHandler)
    
    for port in ports:
        server.