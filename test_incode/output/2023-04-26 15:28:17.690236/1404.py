#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or enumerates user input. """    
    
    # Start webserver
    server = HTTPServer(('', 0), Handler)
    server.serve_forever()
    
    # 