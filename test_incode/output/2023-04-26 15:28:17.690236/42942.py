#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    webserver = HTTPServer(('', 8080), Handler)
    webserver.serve_forever()
