#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and opens all ports. """    
    
    ports = [8080, 8081, 8082]
    
    server = HTTPServer(('', 0), MyHandler)
    
    for port in ports:
        server.