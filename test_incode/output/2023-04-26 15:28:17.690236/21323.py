#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and removes words. """    
    
    ports = range(8000, 8100)
    
    for port in ports:
        
        server = HTTPServer(('0.0.0.0', port), WordsHandler)
        server.serve_forever()
    
