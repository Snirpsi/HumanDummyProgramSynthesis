#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or prints all ports. """    
    
    ports = range(8000, 8100)
    
    for port in ports:
        server = HTTPServer(('0.0.0.0', port), WordsHandler)
        server.serve_forever()
    
