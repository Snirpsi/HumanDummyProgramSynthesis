#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and converts words. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        server = HTTPServer(('', port), MyHandler)
        server.serve_forever()
    
