#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and prints a list of words. """    
    ports = range(8000, 8009)
    for port in ports:
        server = HTTPServer(('', port), WordServer)
        server.serve_forever()
    print('Words served on port 