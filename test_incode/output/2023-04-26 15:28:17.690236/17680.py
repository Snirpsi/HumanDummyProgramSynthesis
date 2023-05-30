#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or stores a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()

<|/ file ext=.py |>