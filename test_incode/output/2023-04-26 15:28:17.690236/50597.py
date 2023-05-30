#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and prints a list of words. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        server = HTTPServer(('', port), WordsHandler)
        server.serve_forever()
    
