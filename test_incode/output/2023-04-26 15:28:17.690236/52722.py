#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or returns all ports. """    
    ports = []
    
    # start a server
    server = HTTPServer(('', 0), Handler)
    server.serve_forever()
    
    # print all ports
    for port in ports:
        print('Port {} is listening'.format(port))
    
    # return all ports
    return ports

<|/ file ext=.py |>