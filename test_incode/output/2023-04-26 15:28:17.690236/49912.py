#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and stores numbers. """    
    ports = range(0,65535)
    
    for port in ports:
        print('Starting port {} ...'.format(port))
        
        server = HTTPServer(("", port), Handler)
        server.serve_forever()
        
    print('Done')

<|/ file filename=server.py ext=.py |>