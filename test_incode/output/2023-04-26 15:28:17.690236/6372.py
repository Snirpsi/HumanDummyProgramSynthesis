#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and returns a port. """    
    port = 8080
    
    # Open a socket to the port and return the port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', port))
    port = s.getsockname()[1]
    s.close()
    return port

<|/ file source=github |>