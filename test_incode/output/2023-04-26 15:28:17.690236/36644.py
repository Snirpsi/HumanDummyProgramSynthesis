#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or converts user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()

<|/ file filename=server.py source=github |>